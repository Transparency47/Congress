# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7249
- Title: Bond Improvement and Reclamation Assurance Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7249
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-02-13T17:32:21Z
- Update date including text: 2026-02-13T17:32:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7249",
    "number": "7249",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Bond Improvement and Reclamation Assurance Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-13T17:32:21Z",
    "updateDateIncludingText": "2026-02-13T17:32:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:33:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7249ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7249\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Deluzio (for himself, Ms. Lee of Pennsylvania , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Surface Mining Control and Reclamation Act of 1977 to establish additional considerations with regard to the adequacy of permit performance bonds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bond Improvement and Reclamation Assurance Act of 2026 .\n#### 2. Surface Mining Control and Reclamation Act of 1977 reform\n##### (a) Permit performance bonds\nSection 509 of the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1259 ) is amended\u2014\n**(1)**\nin subsection (a), to read as follows:\n(a) (1) After a surface coal mining and reclamation permit application has been approved but before such a permit is issued, the applicant shall file with the regulatory authority, on a form prescribed and furnished by the regulatory authority, a bond for performance payable, as appropriate, to the United States or to the State, and conditional upon faithful performance of all the requirements of this Act and the permit. (2) The bond shall cover that area of land within the permit area upon which the operator will initiate and conduct surface coal mining and reclamation operations within the initial term of the permit. (3) As succeeding increments of surface coal mining and reclamation operations are to be initiated and conducted within the permit area, the permittee shall file with the regulatory authority an additional bond to cover such increments in accordance with this section. (4) The amount of the bond required for each bonded area shall\u2014 (A) be determined by the regulatory authority; (B) depend upon the reclamation requirements of the approved permit; (C) reflect the probable difficulty of reclamation giving consideration to factors including topography, geology of the site, hydrology, and revegetation potential; (D) be sufficient to ensure the completion of the reclamation plan if the work had to be performed by the regulatory authority in the event of bond forfeiture; and (E) be set at a level consistent with the rebuttable presumption that the mine will close 5 years after the permit is issued. (5) In setting the amount of the bond under paragraph (4), the regulatory authority shall consider\u2014 (A) the impact of a reasonably expected level of inflation over the time period that the reclamation is likely to occur; (B) the impact of an unplanned or early mine closure on the cost of reclamation, including whether there will be sufficient spoil available to reclaim the mine; and (C) any additional costs likely to be incurred as a result of the regulatory authority undertaking reclamation operations upon bond forfeiture. (6) The amount of a bond for the entire area under 1 permit may not be less than $52,593, annually adjusted for inflation in accordance with the Consumer Price Index for all Urban Consumers, as published by the Bureau of Labor Statistics. ; and\n**(2)**\nin subsection (e), to read as follows:\n(e) The amount of the bond or deposit required and the terms of each acceptance of the bond of the applicant shall be adjusted by the regulatory authority\u2014 (1) from time to time\u2014 (A) as affected land acreages are increased or decreased; or (B) where the cost of future reclamation changes due to changing circumstances, including\u2014 (i) long-term water pollution discharge; (ii) coal market conditions; (iii) unanticipated mine closures; and (iv) changes in the reclamation plan; (2) whenever a permit is renewed; and (3) whenever a permit is transferred to a new operator. .\n##### (b) Revision of permits\nSection 511 of the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1261 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) (1) Before approving a transfer, assignment, or sale of the rights granted under a permit issued pursuant to this Act or an application for a revision of a permit submitted under subsection (a), the regulatory authority shall recalculate the amount of the bond required under section 509 for such permit and require the transferee, assignee, or purchaser of the rights granted under the permit or the permittee, respectively, to post such amount. (2) A permittee and each covered person\u2014 (A) may not be released from liability under the permit; and (B) shall be jointly and severally liable for all reclamation costs incurred by the regulatory authority to complete reclamation under the permit, including treatment of all postmining water pollution. (3) In this subsection, the term covered person means, with respect to a permittee\u2014 (A) a person that owns or otherwise controls 30 percent or more of the capital interests of the permittee; and (B) a person that owns or otherwise controls 30 percent or more of the capital interests of a person described in subparagraph (A). .\n##### (c) Inspections and monitoring\nSection 517 of the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1267 ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nby striking Each inspector and inserting (1) Each inspector ; and\n**(B)**\nby adding at the end the following:\n(2) Each inspector, upon completion of an inspection of any surface coal mining and reclamation operations, shall forthwith inform the regulatory authority of any changes to conditions at such surface coal mining and reclamation operations that may\u2014 (A) result in an unanticipated increase in the cost of reclamation of such surface coal mining and reclamation operations; and (B) necessitate a change to the amount of the bond established for the permit associated with such surface coal mining and reclamation operations under section 509. ; and\n**(2)**\nin subsection (f), by inserting electronically and also after available to the public .\n##### (d) Rulemaking\n**(1) In general**\nNot later than 90 days after the date of the enactment of this section, taking into account the standards in subsections (a) and (e) of section 509 of the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1259 ) regarding bond adequacy, as amended by this section, the Secretary shall issue regulations to establish guidelines and benchmarks for each Federal and State regulatory authority to determine minimum bond amounts under section 509 of that Act ( 30 U.S.C. 1259 ).\n**(2) Data**\nIn issuing the regulations described in paragraph (1), the Secretary shall use data from a representative sample of recent reclamation projects completed by Federal and State regulatory authorities as a result of bond forfeiture by a permittee.\n**(3) Definitions**\nIn this subsection:\n**(A) Regulatory authority**\nThe term regulatory authority has the meaning given the term in section 701 of the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1291 ).\n**(B) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the Office of Surface Mining Reclamation and Enforcement.",
      "versionDate": "2026-01-27",
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
        "name": "Energy",
        "updateDate": "2026-02-13T17:32:20Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7249ih.xml"
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
      "title": "Bond Improvement and Reclamation Assurance Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bond Improvement and Reclamation Assurance Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Surface Mining Control and Reclamation Act of 1977 to establish additional considerations with regard to the adequacy of permit performance bonds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:22Z"
    }
  ]
}
```
