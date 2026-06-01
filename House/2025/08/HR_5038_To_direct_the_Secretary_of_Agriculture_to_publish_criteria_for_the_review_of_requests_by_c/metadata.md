# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5038?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5038
- Title: American Protein Processing Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 5038
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2026-05-16T08:07:51Z
- Update date including text: 2026-05-16T08:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5038",
    "number": "5038",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "American Protein Processing Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:51Z",
    "updateDateIncludingText": "2026-05-16T08:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:52:08Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NE"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "AL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "IA"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "MN"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NE"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "GA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5038ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5038\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Finstad (for himself, Mr. Smith of Nebraska , Mr. Moore of Alabama , Mr. Feenstra , Mrs. Fischbach , Mr. Flood , Mr. Clyde , and Mr. Baird ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to publish criteria for the review of requests by certain meat or poultry establishments to operate at alternate inspection rates, to review and respond to such requests, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Protein Processing Modernization Act .\n#### 2. Requests for alternate inspection rates of meat and poultry\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Secretary of Agriculture (referred to in this section as the Secretary ) shall\u2014\n**(1)**\npublish in the Federal Register food safety criteria that the Secretary shall consider in granting a request submitted by any establishment to operate at alternate inspection rates; and\n**(2)**\nbegin reviewing and responding to such requests from such establishments.\n##### (b) Response\n**(1) In general**\nNot later than 90 days after the date on which a request from an establishment to operate at alternate inspection rates is submitted, the Secretary shall respond\u2014\n**(A)**\nin the case of a request that the Secretary determines meets the food safety criteria referred to in subsection (a)(1), by approving such request; or\n**(B)**\nin the case of a request that the Secretary determines does not meet the food safety criteria referred to in subsection (a)(1), by denying such request in writing and explaining in detail the reasons for such denial.\n**(2) Failure by Secretary to respond**\nIn the case of a failure by the Secretary to respond to a request during the 90-day period referred to in paragraph (1), such request shall be deemed to have been approved by the Secretary.\n##### (c) Continuation of operations at certain establishments\nIn the case of an establishment operating at alternate inspection rates as of the date of enactment of this Act, the Secretary shall authorize such establishment to continue operating at such rates\u2014\n**(1)**\nso long as the establishment maintains effective process control; or\n**(2)**\nuntil such date that the Secretary, under subsection (b)(1), approves or denies a request submitted by the establishment to operate at alternate inspection rates.\n##### (d) Duration of approved requests\nAn establishment may continue to operate pursuant to the terms of a request approved under subsection (b)(1) so long as the establishment continues to meet the food safety criteria referred to in subsection (a)(1).\n##### (e) Noncompliance and revocation\n**(1) Notice of noncompliance**\nThe Secretary shall provide\u2014\n**(A)**\nin the case of an establishment operating pursuant to the terms of a request approved under subsection (b)(1) that fails to meet the food safety criteria referred to in subsection (a)(1), written notice to such establishment describing the nature of such failure; and\n**(B)**\nin the case of an establishment continuing operations under subsection (c) that fails to adhere to the requirements of such subsection, written notice to such establishment describing the nature of such failure.\n**(2) Response to noncompliance**\n**(A) In general**\nFollowing the 180-day period beginning on the date on which an establishment receives a written notice of noncompliance under paragraph (1), if the Secretary determines the establishment has not remedied the failures described in such notice, the Secretary may\u2014\n**(i)**\nat the discretion of the Secretary, provide the establishment an additional opportunity to remedy the failures described in such notice; or\n**(ii)**\nrevoke the authority of the establishment to continue operating at alternate inspection rates and provide written notice to the establishment describing the basis for such revocation.\n**(B) Rule of construction**\nNothing in subparagraph (A) shall be construed to limit the authority of the Secretary to take any action under other statutory or regulatory authority during the 180-day period described in such subparagraph to address food safety noncompliance with respect to an establishment that has received a written notice of noncompliance under paragraph (1).\n**(3) Timeline for adjusting inspection rates**\n**(A) In general**\nThe written notice of revocation referred to in paragraph (2)(A)(ii) shall include a timeline for adjusting inspection rates at the establishment receiving such notice to inspection rates otherwise permitted under regulations implementing the post-mortem inspection requirements of the Federal Meat Inspection Act ( 21 U.S.C. 601 et seq. ) and the Poultry Products Inspection Act (21 U.S.C. et seq.), in effect as of the date of enactment of this Act (or successor regulations).\n**(B) Minimization of negative impacts**\nIn establishing the timeline for adjusting inspection rates described in subparagraph (A), the Secretary shall\u2014\n**(i)**\nconsider potential effects on live animal production and sourcing; and\n**(ii)**\nconsult with the establishment to which such rates shall apply to minimize negative impacts\u2014\n**(I)**\non the ability of the establishment to fulfill any contractual obligations of the establishment in effect on the date on which such timeline is established;\n**(II)**\non animal producers or growers; and\n**(III)**\non animal welfare.\n**(4) Applicability**\nA revocation under paragraph (2)(A)(ii) shall not limit the ability of an establishment to apply and be approved for alternate inspection rates under subsection (b)(1), so long as the establishment otherwise meets the food safety criteria referred to in subsection (a)(1).\n##### (f) Definitions\nIn this section:\n**(1) Alternate inspection rates**\nThe term alternate inspection rates means any rate in excess of the maximum rates permissible under regulations implementing the post-mortem inspection requirements of the Federal Meat Inspection Act ( 21 U.S.C. 601 et seq. ) and the Poultry Products Inspection Act ( 21 U.S.C. 451 et seq. ), in effect as of the date of enactment of this Act (or successor regulations).\n**(2) Establishment**\nThe term establishment means\u2014\n**(A)**\nan official establishment that is subject to inspection under the Federal Meat Inspection Act ( 21 U.S.C. 601 et seq. ); and\n**(B)**\nan official establishment that is subject to inspection under the Poultry Products Inspection Act ( 21 U.S.C. 451 et seq. ).\n##### (g) Rule of construction\nNothing in this section shall be construed to establish any liability or responsibility on the Department of Agriculture or the Food Safety and Inspection Service with respect to\u2014\n**(1)**\nthe safety of establishment workers; or\n**(2)**\nany environmental effects related to alternate inspection rates.",
      "versionDate": "2025-08-26",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-05T17:04:02Z"
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
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5038ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Protein Processing Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-27T08:23:19Z"
    },
    {
      "title": "American Protein Processing Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-27T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to publish criteria for the review of requests by certain meat or poultry establishments to operate at alternate inspection rates, to review and respond to such requests, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-27T08:18:21Z"
    }
  ]
}
```
