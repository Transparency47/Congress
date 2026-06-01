# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/867?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/867
- Title: IGO Anti-Boycott Act
- Congress: 119
- Bill type: HR
- Bill number: 867
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-04-27T16:00:51Z
- Update date including text: 2026-04-27T16:00:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/867",
    "number": "867",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "IGO Anti-Boycott Act",
    "type": "HR",
    "updateDate": "2026-04-27T16:00:51Z",
    "updateDateIncludingText": "2026-04-27T16:00:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NJ"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NE"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "KS"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NE"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr867ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 867\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Lawler (for himself, Mr. Gottheimer , Mr. Weber of Texas , Mr. Ciscomani , Ms. Tenney , Ms. Salazar , Mr. Bacon , Mr. Schmidt , Mr. Fitzpatrick , Mr. Moskowitz , Mr. Wilson of South Carolina , Mr. Hamadeh of Arizona , Mr. Babin , Mr. Morelle , and Mr. Kustoff ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Anti-Boycott Act of 2018 to apply the provisions of that Act to international governmental organizations.\n#### 1. Short title\nThis Act may be cited as the IGO Anti-Boycott Act .\n#### 2. Amendments to the Anti-Boycott Act of 2018\nThe Anti-Boycott Act of 2018 is amended as follows:\n**(1)**\nIn section 1772 ( 50 U.S.C. 4841 ), by inserting , or international governmental organization, after foreign country each place it appears.\n**(2)**\nIn section 1773 ( 50 U.S.C. 4842 ), in subsection (a)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting or international governmental organization, after foreign country, ;\n**(B)**\nin subparagraph (A), in the first sentence, by inserting or international governmental organization after boycotting country ; and\n**(C)**\nin subparagraph (D), in the first sentence, by inserting or international governmental organization after boycotting country .\n**(3)**\nIn section 1773(a) ( 50 U.S.C. 4842(a) ), by adding at the end the following:\n(6) Annual report The President shall submit to Congress and make available to the public on an annual basis a report that contains\u2014 (A) a list of those foreign countries and international organizations that foster or impose boycotts and with respect to which this section applies; and (B) a description of those boycotts. .",
      "versionDate": "2025-01-31",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-15",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "4296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "IGO Anti-Boycott Act",
      "type": "S"
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
        "name": "International Affairs",
        "updateDate": "2025-04-30T17:58:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr867",
          "measure-number": "867",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr867v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>IGO Anti-Boycott Act</strong></p><p>This bill penalizes U.S. persons (individuals or entities) that participate in certain boycotts imposed by international governmental organizations (IGOs).</p><p>The bill expands an existing law that prohibits various actions by U.S. persons in relation to boycotts imposed by foreign governments on a country that is friendly to the United States and not itself the object of a U.S. boycott. This bill applies those prohibitions to similar boycotts imposed by IGOs.</p><p>Prohibited actions include (1) refusing to do business with companies organized under the laws of the boycotted country, if the refusal is pursuant to an agreement with or request from the country or IGO imposing the boycott; (2) furnishing information about whether any person has a business relationship with or in the boycotted country; and (3) furnishing information about whether someone is associated with charitable or fraternal organizations that support the boycotted country.</p><p>Criminal penalties for willful violations of this law include fines of up to $1 million. In addition to such fines, individuals may be imprisoned for up to 20 years. Civil penalties may include fines and revocations of export licenses for certain national security-related items.</p><p>The bill also requires the President to annually submit to Congress and make available to the public a report describing these boycotts and listing the foreign countries and international organizations involved in fostering or imposing them.</p>"
        },
        "title": "IGO Anti-Boycott Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr867.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IGO Anti-Boycott Act</strong></p><p>This bill penalizes U.S. persons (individuals or entities) that participate in certain boycotts imposed by international governmental organizations (IGOs).</p><p>The bill expands an existing law that prohibits various actions by U.S. persons in relation to boycotts imposed by foreign governments on a country that is friendly to the United States and not itself the object of a U.S. boycott. This bill applies those prohibitions to similar boycotts imposed by IGOs.</p><p>Prohibited actions include (1) refusing to do business with companies organized under the laws of the boycotted country, if the refusal is pursuant to an agreement with or request from the country or IGO imposing the boycott; (2) furnishing information about whether any person has a business relationship with or in the boycotted country; and (3) furnishing information about whether someone is associated with charitable or fraternal organizations that support the boycotted country.</p><p>Criminal penalties for willful violations of this law include fines of up to $1 million. In addition to such fines, individuals may be imprisoned for up to 20 years. Civil penalties may include fines and revocations of export licenses for certain national security-related items.</p><p>The bill also requires the President to annually submit to Congress and make available to the public a report describing these boycotts and listing the foreign countries and international organizations involved in fostering or imposing them.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr867"
    },
    "title": "IGO Anti-Boycott Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IGO Anti-Boycott Act</strong></p><p>This bill penalizes U.S. persons (individuals or entities) that participate in certain boycotts imposed by international governmental organizations (IGOs).</p><p>The bill expands an existing law that prohibits various actions by U.S. persons in relation to boycotts imposed by foreign governments on a country that is friendly to the United States and not itself the object of a U.S. boycott. This bill applies those prohibitions to similar boycotts imposed by IGOs.</p><p>Prohibited actions include (1) refusing to do business with companies organized under the laws of the boycotted country, if the refusal is pursuant to an agreement with or request from the country or IGO imposing the boycott; (2) furnishing information about whether any person has a business relationship with or in the boycotted country; and (3) furnishing information about whether someone is associated with charitable or fraternal organizations that support the boycotted country.</p><p>Criminal penalties for willful violations of this law include fines of up to $1 million. In addition to such fines, individuals may be imprisoned for up to 20 years. Civil penalties may include fines and revocations of export licenses for certain national security-related items.</p><p>The bill also requires the President to annually submit to Congress and make available to the public a report describing these boycotts and listing the foreign countries and international organizations involved in fostering or imposing them.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr867"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr867ih.xml"
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
      "title": "IGO Anti-Boycott Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IGO Anti-Boycott Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Anti-Boycott Act of 2018 to apply the provisions of that Act to international governmental organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:18:26Z"
    }
  ]
}
```
