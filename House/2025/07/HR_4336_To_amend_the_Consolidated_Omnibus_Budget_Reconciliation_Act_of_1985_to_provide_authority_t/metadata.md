# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4336?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4336
- Title: CBP SPACE Act
- Congress: 119
- Bill type: HR
- Bill number: 4336
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-09-15T16:40:02Z
- Update date including text: 2025-09-15T16:40:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4336",
    "number": "4336",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CBP SPACE Act",
    "type": "HR",
    "updateDate": "2025-09-15T16:40:02Z",
    "updateDateIncludingText": "2025-09-15T16:40:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "WA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-10",
      "state": "LA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "ME"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4336ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4336\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Lee of Florida (for herself, Ms. Perez , Ms. Brownley , Mr. Buchanan , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Consolidated Omnibus Budget Reconciliation Act of 1985 to provide authority to adjust the rate of merchandise processing fees to offset the capital costs incurred by U.S. Customs and Border Protection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CBP SPACE Act .\n#### 2. Authority to adjust the rate of merchandise processing fees to offset the capital costs incurred by U.S. Customs and Border Protection; modification to disposition of customs user fees\n##### (a) In general\nSection 13031 of the Consolidated Omnibus Budget Reconciliation Act of 1985 ( 19 U.S.C. 58c ) is amended\u2014\n**(1)**\nin subsection (a)(9)(B)(i), by striking salaries and expenses and inserting salaries, expenses, and capital costs ; and\n**(2)**\nin subsection (f)(3)(A)(i)\u2014\n**(A)**\nin subclause (IV), by striking , and at the end;\n**(B)**\nin subclause (V), by striking the comma at the end and inserting , and ; and\n**(C)**\nby adding at the end the following:\n(VI) paying capital costs associated with passenger inspection services, .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.\n##### (c) Sense of congress\nIt is the sense of Congress that the Secretary of the Treasury and the Commissioner of U.S. Customs and Border Protection should work jointly to set an appropriate level for merchandise processing fees charged and collected under 13031 of the Consolidated Omnibus Budget Reconciliation Act of 1985 ( 19 U.S.C. 58c ), as amended by subsection (a), such that U.S. Customs and Border Protection is able to adequately fund equipment upgrades and facilities construction, improvement, and maintenance at United States sea ports of entry.\n#### 3. Prohibition on provision or maintenance of administrative, training, or recreational facilities at sea ports of entry for U.S. Customs and Border Protection\n##### (a) In general\nThe Commissioner of U.S. Customs and Border Protection may not request or otherwise require a sea port of entry to provide or maintain administrative, training, or recreational facilities at the port of entry for purposes of facilitating inspection services of U.S. Customs and Border Protection.\n##### (b) Rule of construction\nNothing in this section shall be construed to modify or otherwise affect the authority contained in section 482 of the Homeland Security Act of 2002 ( 6 U.S.C. 301a ).\n#### 4. Annual report on use of proceeds of merchandise processing fee\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Commissioner of U.S. Customs and Border Protection shall submit to the appropriate congressional committees a report\u2014\n**(1)**\nspecifying the amount of proceeds from the merchandise processing fee collected under section 13031(a)(9) of the Consolidated Omnibus Budget Reconciliation Act of 1985, as amended by section 1, during the year preceding submission of the report;\n**(2)**\nspecifying the amount of such proceeds directed to inspection facilities at sea ports of entry; and\n**(3)**\ndescribing the outstanding capital needs of such inspection facilities.\n##### (b) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Finance, the Committee on Homeland Security and Governmental Affairs, and the Committee on Appropriations of the Senate; and\n**(2)**\nthe Committee on Ways and Means, the Committee on Homeland Security, and the Committee on Appropriations of the House of Representatives.",
      "versionDate": "2025-07-10",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T16:40:02Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4336ih.xml"
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
      "title": "CBP SPACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CBP SPACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Omnibus Budget Reconciliation Act of 1985 to provide authority to adjust the rate of merchandise processing fees to offset the capital costs incurred by U.S. Customs and Border Protection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:25Z"
    }
  ]
}
```
