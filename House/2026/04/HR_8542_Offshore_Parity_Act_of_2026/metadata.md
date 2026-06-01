# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8542
- Title: Offshore Parity Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8542
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-30T08:05:42Z
- Update date including text: 2026-05-30T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-29 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-29 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8542",
    "number": "8542",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Offshore Parity Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:42Z",
    "updateDateIncludingText": "2026-05-30T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-04-28T13:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-29T21:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "LA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "AL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8542ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8542\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mr. Ezell (for himself, Mr. Higgins of Louisiana , Mr. Carter of Louisiana , and Mr. Figures ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Outer Continental Shelf Lands Act and the Magnuson-Stevens Fishery Conservation and Management Act to provide for the delegation of authority to Louisiana, Mississippi, and Alabama to manage certain expanded submerged lands, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Offshore Parity Act of 2026 .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto provide equity to the States of Louisiana, Mississippi, and Alabama with respect to the seaward boundaries of the States in the Gulf of America by delegating management of the submerged lands from 3 geographical miles to 3 marine leagues if the States meet certain conditions not later than 5 years after the date of enactment of this Act;\n**(2)**\nin delegating the authority to administer any leases, easements, rights-of-use, and rights-of-way, the States shall ensure that the rights of lessees, operators, and holders of leases, easements, rights-of-use, and rights-of-way on the submerged land are protected; and\n**(3)**\nto improve the management of fisheries by allowing the States of Louisiana, Mississippi, and Alabama to oversee fisheries management in the expanded seaward boundaries.\n#### 3. Delegation of the management of oil, gas, and other energy activities on the expanded submerged land of Louisiana, Mississippi, and Alabama\n##### (a) Delegation\nThe Outer Continental Shelf Lands Act ( 42 U.S.C. 1301 et seq. ) is amended by adding at the end the following:\n34. Delegation of the management of oil, gas, and other energy activities on the expanded submerged land of Louisiana, Mississippi, and Alabama (a) Definitions In this section: (1) Coast line The term coast line has the meaning given such term in section 2 of the Submerged Lands Act ( 43 U.S.C. 1301 ). (2) Expanded submerged land The term expanded submerged land means the area of the outer Continental Shelf that is located between 3 geographical miles and 3 marine leagues seaward of the coast line of the State as of the day before the date of the enactment of this section. (3) Secretary The term Secretary means the Secretary of the Interior. (4) State The term State means Louisiana, Mississippi, or Alabama. (b) Delegation Upon written request of a State before the date that is 5 years after the date of enactment of the Offshore Parity Act of 2026 , the Secretary shall, except as provided in subsection (c), delegate to the State the relevant authorities of the Secretary under this Act, except the authority under sections 14 and 20, to grant and manage leases of the expanded submerged land of the State if the Secretary finds that\u2014 (1) it is likely the State will provide adequate resources to carry out such authorities; (2) the State has demonstrated that it will effectively and faithfully administer the applicable rules and regulations of the Secretary under this Act, including the requirements of subsection (c) of this section; and (3) such delegation will not create an unreasonable burden on any lessee. (c) Requirements (1) No lease or tract divided The Secretary may not delegate authority under this section with respect to any lease of an area that is not wholly located within the expanded submerged land of the State. (2) Applicability to existing leases The delegation of authority under this section shall apply to any lease of the expanded submerged land of the State granted by the Secretary before the date of enactment of the Offshore Parity Act of 2026 . (3) No 5 year plan required A State to which authority is delegated under this section shall not be required to prepare, revise, or maintain an oil and gas leasing program under section 18. (4) Revenue (A) Rentals, royalties, and other sums A State to which authority is delegated under this section may collect rentals, royalties, and other sums, as determined by the State, from any lease granted after the date of enactment of the Offshore Parity Act of 2026 by the State under such authority. (B) Minimum bid and royalty amounts The minimum bid and royalty amounts under section 8 shall not apply to any lease of the expanded submerged land of the State granted by the State after the date of enactment of the Offshore Parity Act of 2026 . (C) Disposition of revenue (i) Existing leases The delegation of authority under this section shall not affect the disposition of revenue under any other provision of Federal law from any lease of the expanded submerged land of the State granted before the date of enactment of the Offshore Parity Act of 2026 . (ii) New leases Section 9 of this Act and section 105 of the Gulf of Mexico Energy Security Act of 2006 shall not apply with respect to a lease granted after the date of enactment of the Offshore Parity Act of 2026 by a State under authority delegated under this section. (5) Citizen suits, court jurisdiction, and judicial review Section 23 shall not apply with respect to a lease granted after the date of enactment of the Offshore Parity Act of 2026 by a State under authority delegated under this section. (6) Liability (A) In general A State to which authority is delegated by the Secretary under this section shall indemnify the United States for any liability to any holder of an oil, gas, or other energy lease of the expanded submerged land of the State granted before such delegation of authority from the taking of any property interest or breach of contract as a result of\u2014 (i) the delegation of such authority; or (ii) the management of any such lease. (B) Deduction from oil and gas leasing revenues The Secretary may deduct from the amounts otherwise payable to a State under section 8(g)(2) the amount of any final nonappealable judgment for a taking or breach of contract by such State described in subparagraph (A). (7) Transfer of bonds (A) In general Not later than 90 days after delegating authority under this section, the Secretary shall transfer any surety bonds for oil, gas, or other energy leases of the expanded submerged land of a State granted before the date of enactment of the Offshore Parity Act of 2026 to the applicable State. The applicable State shall ensure that any decommissioning of a facility with respect to such leases is carried out in accordance with applicable Federal law, including regulations. (B) Failure to transfer bonds If the Secretary does not transfer a surety bond for a lease under subparagraph (A) by the deadline described in such subparagraph, the Secretary shall ensure that any decommissioning of a facility with respect to such lease is carried out in accordance with applicable Federal law, including regulations. .\n##### (b) Seaward boundary of louisiana, mississippi, and alabama\nSection 8(g) of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1337(g) ) is amended by adding at the end the following:\n(8) Definition of seaward boundary of Louisiana, Mississippi, and Alabama In this subsection, the term seaward boundary means, with respect to each of the States of Louisiana, Mississippi, and Alabama, 3 marine leagues seaward of the coast line (as that term is defined in section 2 of the Submerged Lands Act ( 43 U.S.C. 1301 )) of each such State as each such coast line exists as of the day before the date of the enactment of this paragraph. .\n#### 4. State jurisdiction under Magnuson-Stevens Fishery Conservation and Management Act\n##### (a) In general\nSection 306(a)(2) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1856(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C)(ii), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) with respect to each of the States of Alabama, Louisiana, and Mississippi, to 3 marine leagues seaward of the coast line (as that term is defined in section 2 of the Submerged Lands Act ( 43 U.S.C. 1301 )) of each such State as each such coast line exists as of the day before the date of the enactment of this subparagraph. .\n##### (b) Rules of construction\n**(1) Highly migratory species**\nThe amendments made by this section may not be construed to limit or otherwise affect the authority of the Federal Government with respect to highly migratory species, species listed as a threatened species or an endangered species pursuant to the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), or fishery resources subject to international agreements as provided under Federal law, including the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ), the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), and relevant international treaties.\n**(2) Federal jurisdiction**\nThe amendments made by this section may not be construed to limit or otherwise affect the authority of the Federal Government under the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ) with respect to\u2014\n**(A)**\nthe exclusive economic zone beyond the extended State waters of a covered State; or\n**(B)**\nactivities within the extended State waters of a covered State that relate to national security, international obligations, or other matters reserved for Federal authority.\n##### (c) Definitions\nIn this section:\n**(1) Coast line**\nThe term coast line has the meaning given the term in section 2 of the Submerged Lands Act ( 43 U.S.C. 1301 ).\n**(2) Covered state**\nThe term covered State means each of the States of Alabama, Louisiana, and Mississippi.\n**(3) Exclusive economic zone**\nThe term exclusive economic zone has the meaning given the term in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 ).\n**(4) Extended state waters**\nThe term extended State waters means 3 marine leagues seaward of the coast line of a covered State as each such coast line exists as of the day before the date of the enactment of this section.\n**(5) Fishery resource**\nThe term fishery resource has the meaning given the term in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 ).\n**(6) Highly migratory species**\nThe term highly migratory species has the meaning given the term in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 ).",
      "versionDate": "2026-04-28",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-08T20:40:24Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8542ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Offshore Parity Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T08:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Offshore Parity Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Outer Continental Shelf Lands Act and the Magnuson-Stevens Fishery Conservation and Management Act to provide for the delegation of authority to Louisiana, Mississippi, and Alabama to manage certain expanded submerged lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T08:03:35Z"
    }
  ]
}
```
