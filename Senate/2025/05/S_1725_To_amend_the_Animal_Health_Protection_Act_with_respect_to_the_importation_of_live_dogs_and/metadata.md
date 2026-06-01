# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1725?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1725
- Title: Healthy Dog Importation Act
- Congress: 119
- Bill type: S
- Bill number: 1725
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2026-02-18T13:41:03Z
- Update date including text: 2026-02-18T13:41:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1725",
    "number": "1725",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Healthy Dog Importation Act",
    "type": "S",
    "updateDate": "2026-02-18T13:41:03Z",
    "updateDateIncludingText": "2026-02-18T13:41:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-05-13T16:32:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-13T16:32:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "KS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "MS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "ID"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "KS"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "GA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-17",
      "state": "ME"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NJ"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1725is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1725\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Grassley (for himself, Ms. Smith , Mr. Marshall , Mrs. Hyde-Smith , Mr. Risch , Ms. Ernst , Mr. Moran , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Animal Health Protection Act with respect to the importation of live dogs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Dog Importation Act .\n#### 2. Importation of live dogs\n##### (a) In general\nThe Animal Health Protection Act ( 7 U.S.C. 8301 et seq. ) is amended by inserting after section 10404 ( 7 U.S.C. 8303 ) the following:\n10404A. Importation of live dogs (a) Definitions In this section: (1) Compensation The term compensation means any act, consideration, or thing of value received by a person directly, including cash or noncash benefits, cost-avoidance, obtaining positive or avoiding negative publicity, an exchange of services, or maintaining a license issued under any local, State, or Federal government authority. (2) Import transporter The term import transporter means any person or entity that\u2014 (A) receives an imported dog from any importer, dealer, research facility, exhibitor, operator of an auction sale, or department, agency, or instrumentality of the United States or of any State or local government; and (B) receives compensation for moving such dog in commerce. (3) Importer The term importer means any person who transports or causes the transportation of a dog into the United States from a foreign country. (4) Transfer The term transfer means a change of ownership or control of an imported dog to another person, including by sale, adoption, exchange, or donation. (b) Requirements (1) In general Except as provided in paragraph (2), no person shall import a dog into the United States unless prior to transport to the United States, the Secretary receives electronic documentation necessary, as determined by the Secretary, to demonstrate that the dog\u2014 (A) is in good health; (B) has received all necessary vaccinations and internal and external parasite treatment, and demonstrated negative test results, as required by the Secretary and evidenced by a certificate that\u2014 (i) is issued by a licensed veterinarian accredited by a competent veterinary authority recognized by the Secretary; and (ii) is endorsed by that authority in a manner representing that the veterinarian issuing the certificate was authorized to do so; (C) is officially identified by a permanent method approved by the Secretary; and (D) in the case that the dog is intended for transfer\u2014 (i) is at least 6 months old; and (ii) is accompanied by an import permit issued by the Secretary under this Act. (2) Exceptions The Secretary, by regulation, shall provide an exception to any requirement under this Act in any case in which a dog is imported for purposes of transfer\u2014 (A) as a personal pet of United States origin returning to the United States; (B) as a United States military working dog or contracted working dog supporting a military mission or tasking; (C) for research purposes; (D) for veterinary treatment which is paid for by the importer, subject to the condition that the dog\u2014 (i) is taken directly to a veterinary facility for treatment with appropriate quarantine until the dog meets the criteria described in paragraph (1); and (ii) is then exported to its country of origin; or (E) in the case of a dog that is less than 6 months old, for lawful importation into the State of Hawaii from the British Isles, Australia, Guam, or New Zealand in compliance with the regulations of the State of Hawaii and the other requirements of this section, if the dog is not transported out of the State of Hawaii for transfer at less than 6 months of age. (c) Implementation and regulations Not later than 18 months after the date of enactment of the Healthy Dog Importation Act , the Secretary, in consultation with the Secretary of Health and Human Services, the Secretary of Commerce, the Secretary of Homeland Security, and the Secretary of Transportation, shall promulgate such regulations as the Secretary determines necessary to implement and enforce this section, including regulations\u2014 (1) to facilitate electronic submission and interagency sharing of all documentation required prior to the importation of a dog into the United States under subsection (b)(1); (2) to establish any necessary post-arrival verification processes for imported dogs; (3) to ensure the denial of entry into the United States of any dog attempted to be imported into the United States in violation of subsection (b)(1); (4) to provide that each importer, import transporter, intermediate handler, or carrier receiving a certificate of veterinary inspection required under this section shall submit a copy of the certificate to the Secretary, who shall, upon receipt, record and maintain the information in a centralized database and, upon request by a State veterinarian, share the information with such State veterinarian within 3 days; (5) to require the Secretary to annually report aggregated data submitted under paragraph (4), including information on country of origin and purpose of import; and (6) to determine and establish such fees for the verification of documentation and issuance of permits required under subsection (b)(1) as may be necessary to fund the implementation and enforcement of this section. (d) Rule of construction Nothing in subsection (c)(6) shall be construed as limiting the availability of funding made available under section 10417 to carry out this section. (e) Enforcement (1) Authority The Secretary shall have the authority granted under section 10414 to enforce this section. (2) Penalties An importer or import transporter that fails to comply with this section shall\u2014 (A) be subject to penalties under section 10414; and (B) provide, as the Secretary may determine, at the expense of the importer or import transporter, for\u2014 (i) the care (including appropriate veterinary care), forfeiture, quarantine, and removal from the United States of each applicable dog; and (ii) the return of each applicable dog to its place of export, with due care for the welfare of each applicable dog. .\n##### (b) Transition period\n**(1) In general**\nDuring the transition period, regulations promulgated under section 18 of the Animal Welfare Act ( 7 U.S.C. 2148 ) (as in effect on the day before the date of enactment of this Act) relating to the importation of live dogs shall continue to apply to the extent that such regulations do not conflict with section 10404A of the Animal Health Protection Act (as inserted by subsection (a)).\n**(2) Transition period defined**\nIn this subsection, the term transition period means the period beginning on the date of enactment of this Act and ending on the date on which final regulations are promulgated under such section 10404A.\n##### (c) Conforming amendment\nSection 18 of the Animal Welfare Act ( 7 U.S.C. 2148 ) is repealed.",
      "versionDate": "2025-05-13",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3349",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthy Dog Importation Act",
      "type": "HR"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-06T10:34:29Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1725is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Healthy Dog Importation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Dog Importation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Animal Health Protection Act with respect to the importation of live dogs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:28Z"
    }
  ]
}
```
