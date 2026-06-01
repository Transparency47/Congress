# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/902
- Title: RECOGNIZING Judea and Samaria Act
- Congress: 119
- Bill type: HR
- Bill number: 902
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-05T22:02:25Z
- Update date including text: 2025-12-05T22:02:25Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/902",
    "number": "902",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "RECOGNIZING Judea and Samaria Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:02:25Z",
    "updateDateIncludingText": "2025-12-05T22:02:25Z"
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
          "date": "2025-01-31T15:08:20Z",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NE"
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
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "OK"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr902ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 902\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Tenney (for herself, Mr. Weber of Texas , Mrs. Miller of Illinois , Mr. Moore of Alabama , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the use of materials that use the term West Bank , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Retiring the Egregious Confusion Over the Genuine Name of Israel\u2019s Zone of Influence by Necessitating Government-use of Judea and Samaria Act or the RECOGNIZING Judea and Samaria Act .\n#### 2. Sense of Congress\nIt is the sense of the Congress that the United States Government\u2014\n**(1)**\nshould refer to the land annexed by Israel from Jordan during the 1967 Six-Day War by its historical names of Judea and Samaria , with the land south of Jerusalem being considered Judea and the land north of Jerusalem being considered Samaria ; and\n**(2)**\nshould no longer use the term \u201cWest Bank\u201d in official government materials.\n#### 3. Prohibition on use of materials that use the term West Bank\n##### (a) In general\nNotwithstanding any other provision of law, none of the funds authorized to be appropriated or otherwise made available after the date of the enactment of this Act may be obligated or expended to prepare or promulgate any policy, guidance, regulation, notice, Executive order, materials, briefing, press release, communications, or other work product that refers to Judea and Samaria as the West Bank .\n##### (b) Exception\nThe prohibition in this section shall not apply with respect to the obligation or expenditure of funds relating to obligations of the United States under international treaties or other agreements.\n##### (c) Waiver\nThe Secretary of State may waive the prohibition in this section if the Secretary\u2014\n**(1)**\ndetermines that is in the interests of the United States to do so; and\n**(2)**\nsubmits to Congress an explanation for the waiver not later than 30 days after the date on which the Secretary makes the determination.\n#### 4. Conforming changes to United States law\n##### (a) Foreign Assistance Act of 1961\nThe Foreign Assistance Act of 1961 is amended as follows:\n**(1)**\nIn section 620K(f)(3) ( 22 U.S.C. 2378b(f)(3) ), by striking the West Bank and inserting Judea and Samaria .\n**(2)**\nIn section 620L ( 22 U.S.C. 2378c )\u2014\n**(A)**\nin the section heading, by striking the west bank and inserting judea and samaria ; and\n**(B)**\nby striking the West Bank each place it appears and inserting Judea and Samaria .\n##### (b) Taylor Force Act\nSection 1004 of the Taylor Force Act ( 22 U.S.C. 2378c\u20131 ) is amended\u2014\n**(1)**\nin the section heading, by striking the west bank and inserting judea and samaria ;\n**(2)**\nby striking the West Bank each place it appears and inserting Judea and Samaria .\n##### (c) Multinational Force and Observers Participation Resolution\nSection 2 of the Multinational Force and Observers Participation Resolution ( 22 U.S.C. 3421 ) is amended by striking the West Bank and inserting Judea and Samaria .\n##### (d) Omnibus Diplomatic Security and Antiterrorism Act of 1986\nSection 414 of the Omnibus Diplomatic Security and Antiterrorism Act of 1986 ( 22 U.S.C. 4862 ) is amended\u2014\n**(1)**\nin the section heading, by striking west bank and inserting judea and samaria ; and\n**(2)**\nby striking the West Bank and inserting Judea and Samaria .\n##### (e) United States-Israel Free Trade Area Implementation Act of 1985\nSection 9 of the United States-Israel Free Trade Area Implementation Act of 1985 ( 19 U.S.C. 2112 note) is amended by striking the West Bank each place it appears and inserting Judea and Samaria .\n##### (f) Implementing Recommendations of the 9/11 Commission Act of 2007\nSection 2021(i) of the Implementing Recommendations of the 9/11 Commission Act of 2007 ( 22 U.S.C. 2151 note) is amended by striking the West Bank and inserting Judea and Samaria .\n##### (g) Foreign Relations Authorization Act, Fiscal Year 2003\nSection 699 of the Foreign Relations Authorization Act, Fiscal Year 2003 ( 22 U.S.C. 2301 note) is amended\u2014\n**(1)**\nin the section heading, by striking west bank and inserting judea and samaria ; and\n**(2)**\nin subsection (a), by striking the West Bank and inserting Judea and Samaria .\n##### (h) Nita M. Lowey Middle East Partnership for Peace Act\nSection 8005 of the Nita M. Lowey Middle East Partnership for Peace Act (Pub. L. 116\u2013260) is amended by striking the West Bank each place it appears and inserting Judea and Samaria .",
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
        "actionDate": "2025-02-04",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "384",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RECOGNIZING Judea and Samaria Act",
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
        "updateDate": "2025-05-02T16:09:12Z"
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
          "measure-id": "id119hr902",
          "measure-number": "902",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-07-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr902v00",
            "update-date": "2025-07-12"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Retiring the Egregious Confusion Over the Genuine Name of Israel\u2019s Zone of Influence by Necessitating Government-use of Judea and Samaria Act or the RECOGNIZING Judea and Samaria Act</strong></p><p>This bill prohibits the use of federal funds to prepare or promulgate certain materials (including any policy, guidance, regulation, executive order, or other work products) that refers to Judea and Samaria as the West Bank. The prohibition does not apply to U.S. obligations under international treaties or other agreements.</p><p>The bill also amends certain laws to replace the term <em>the West Bank</em> with <em>Judea and Samaria</em>.</p>"
        },
        "title": "RECOGNIZING Judea and Samaria Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr902.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Retiring the Egregious Confusion Over the Genuine Name of Israel\u2019s Zone of Influence by Necessitating Government-use of Judea and Samaria Act or the RECOGNIZING Judea and Samaria Act</strong></p><p>This bill prohibits the use of federal funds to prepare or promulgate certain materials (including any policy, guidance, regulation, executive order, or other work products) that refers to Judea and Samaria as the West Bank. The prohibition does not apply to U.S. obligations under international treaties or other agreements.</p><p>The bill also amends certain laws to replace the term <em>the West Bank</em> with <em>Judea and Samaria</em>.</p>",
      "updateDate": "2025-07-12",
      "versionCode": "id119hr902"
    },
    "title": "RECOGNIZING Judea and Samaria Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Retiring the Egregious Confusion Over the Genuine Name of Israel\u2019s Zone of Influence by Necessitating Government-use of Judea and Samaria Act or the RECOGNIZING Judea and Samaria Act</strong></p><p>This bill prohibits the use of federal funds to prepare or promulgate certain materials (including any policy, guidance, regulation, executive order, or other work products) that refers to Judea and Samaria as the West Bank. The prohibition does not apply to U.S. obligations under international treaties or other agreements.</p><p>The bill also amends certain laws to replace the term <em>the West Bank</em> with <em>Judea and Samaria</em>.</p>",
      "updateDate": "2025-07-12",
      "versionCode": "id119hr902"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr902ih.xml"
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
      "title": "RECOGNIZING Judea and Samaria Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RECOGNIZING Judea and Samaria Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Retiring the Egregious Confusion Over the Genuine Name of Israel\u2019s Zone of Influence by Necessitating Government-use of Judea and Samaria Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of materials that use the term \"West Bank\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:19Z"
    }
  ]
}
```
