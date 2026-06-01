# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1367
- Title: ELITE Vehicles Act
- Congress: 119
- Bill type: HR
- Bill number: 1367
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-12-05T21:54:36Z
- Update date including text: 2025-12-05T21:54:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1367",
    "number": "1367",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "ELITE Vehicles Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:54:36Z",
    "updateDateIncludingText": "2025-12-05T21:54:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:31:00Z",
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
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "KS"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "NE"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "IA"
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
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "IN"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "AL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "NY"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "ND"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1367ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1367\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Arrington (for himself, Mr. Estes , Ms. Van Duyne , Mr. Ellzey , Mr. Smith of Nebraska , Mr. Feenstra , Mr. Weber of Texas , Mr. Yakym , Mr. Moran , Mr. Palmer , Ms. Tenney , and Ms. Fedorchak ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the credit for new clean vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act .\n#### 2. Repeal of clean vehicle credit\n##### (a) In general\nSubpart B of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 30D (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendments\n**(1)**\nSection 30B(d)(3) of the Internal Revenue Code of 1986 is amended by striking subparagraph (D).\n**(2)**\nSection 38(b) of such Code is amended by striking paragraph (30).\n**(3)**\nSection 179D(d) of such Code is amended\u2014\n**(A)**\nin paragraph (3)(B)(ii), by striking (as defined in section 30D(g)(9)) , and\n**(B)**\nby adding at the end the following new paragraph:\n(6) Indian tribal government For purposes of this subsection, the term Indian tribal government means the recognized governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of this paragraph pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). .\n**(4)**\nSection 1016(a) of such Code is amended\u2014\n**(A)**\nin paragraph (36), by adding and at the end,\n**(B)**\nby striking paragraph (37), and\n**(C)**\nby redesignating paragraph (38) as paragraph (37).\n**(5)**\nSection 6213(g)(2) of such Code is amended by striking subparagraph (T).\n**(6)**\nSection 6417(d)(1)(A)(iv) of such Code is amended by striking section 30D(g)(9) and inserting section 179D(d)(6) .\n**(7)**\nSection 6501(m) of such Code is amended by striking 30D(f)(6), .\n**(8)**\nSection 166(b)(5)(A)(ii) of title 23, United States Code, is amended by inserting , as in effect on the date of the enactment of the ELITE Vehicles Act after section 30D(d)(1) of the Internal Revenue Code of 1986 .\n##### (c) Effective date\nThe amendments made by this section shall apply to vehicles purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.\n#### 3. Repeal of credit for previously-owned clean vehicles\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 25E (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendment\nSection 6213(g)(2) of the Internal Revenue Code of 1986 is amended by striking subparagraph (U).\n##### (c) Effective date\nThe amendments made by this section shall apply to vehicles purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.\n#### 4. Repeal of credit for qualified commercial clean vehicles\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 45W (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendments\n**(1)**\nSection 38(b) of the Internal Revenue Code of 1986, as amended by sections 13502, 13701, and 13704 of Public Law 117\u2013169 , is amended\u2014\n**(A)**\nby striking paragraph (37), and\n**(B)**\nby redesignating paragraphs (38) through (41) as paragraphs (37) through (40), respectively.\n**(2)**\nSection 6213(g)(2) of such Code is amended\u2014\n**(A)**\nby adding and at the end of subparagraph (R),\n**(B)**\nby striking the comma at the end of subparagraph (S) and inserting a period, and\n**(C)**\nby striking subparagraph (V).\n##### (c) Effective date\nThe amendments made by this section shall apply to vehicles purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.\n#### 5. Exclusion of electric vehicle recharging property from alternative fuel vehicle refueling property credit\n##### (a) In general\nSection 30C of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(B), by striking clause (iii), and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Exclusion of electric vehicle recharging property The term qualified alternative fuel vehicle refueling property shall not include any property for the recharging of motor vehicles propelled by electricity. , and\n**(2)**\nby striking subsection (f).\n##### (b) Effective date\nThe amendments made by this section shall apply to property purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.",
      "versionDate": "2025-02-14",
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
        "actionDate": "2025-02-12",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "541",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ELITE Vehicles Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T12:46:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1367",
          "measure-number": "1367",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1367v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act</strong></p><p>This bill eliminates federal tax credits for the purchase of certain clean vehicles (generally electric vehicles and plug-in hybrid vehicles) and electric\u00a0vehicle recharging stations.</p><p>Specifically, the bill repeals the federal tax credits for</p><ul><li>the purchase of a qualified used clean vehicle (tax credit of up to $4,000 for the purchase of a previously-owned clean vehicle before 2033),</li><li>the purchase of a qualified new clean vehicle (tax credit of up to $7,500 for the purchase of a new clean vehicle before 2033),</li><li>the purchase of a qualified commercial clean vehicle (business tax credit of up to $40,000 for the purchase of a commercial clean vehicle before 2033), and</li><li>alternative fuel vehicle refueling property used to recharge electric vehicles (tax credit of up to $1,000 for individuals or up to $100,000 for businesses for the installation of property before 2033 that is used to recharge electric vehicles).</li></ul>"
        },
        "title": "ELITE Vehicles Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1367.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act</strong></p><p>This bill eliminates federal tax credits for the purchase of certain clean vehicles (generally electric vehicles and plug-in hybrid vehicles) and electric\u00a0vehicle recharging stations.</p><p>Specifically, the bill repeals the federal tax credits for</p><ul><li>the purchase of a qualified used clean vehicle (tax credit of up to $4,000 for the purchase of a previously-owned clean vehicle before 2033),</li><li>the purchase of a qualified new clean vehicle (tax credit of up to $7,500 for the purchase of a new clean vehicle before 2033),</li><li>the purchase of a qualified commercial clean vehicle (business tax credit of up to $40,000 for the purchase of a commercial clean vehicle before 2033), and</li><li>alternative fuel vehicle refueling property used to recharge electric vehicles (tax credit of up to $1,000 for individuals or up to $100,000 for businesses for the installation of property before 2033 that is used to recharge electric vehicles).</li></ul>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr1367"
    },
    "title": "ELITE Vehicles Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act</strong></p><p>This bill eliminates federal tax credits for the purchase of certain clean vehicles (generally electric vehicles and plug-in hybrid vehicles) and electric\u00a0vehicle recharging stations.</p><p>Specifically, the bill repeals the federal tax credits for</p><ul><li>the purchase of a qualified used clean vehicle (tax credit of up to $4,000 for the purchase of a previously-owned clean vehicle before 2033),</li><li>the purchase of a qualified new clean vehicle (tax credit of up to $7,500 for the purchase of a new clean vehicle before 2033),</li><li>the purchase of a qualified commercial clean vehicle (business tax credit of up to $40,000 for the purchase of a commercial clean vehicle before 2033), and</li><li>alternative fuel vehicle refueling property used to recharge electric vehicles (tax credit of up to $1,000 for individuals or up to $100,000 for businesses for the installation of property before 2033 that is used to recharge electric vehicles).</li></ul>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr1367"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1367ih.xml"
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
      "title": "ELITE Vehicles Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ELITE Vehicles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eliminate Lavish Incentives To Electric Vehicles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the credit for new clean vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T04:18:29Z"
    }
  ]
}
```
