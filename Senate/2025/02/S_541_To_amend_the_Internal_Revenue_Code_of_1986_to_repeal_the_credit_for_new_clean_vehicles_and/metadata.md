# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/541?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/541
- Title: ELITE Vehicles Act
- Congress: 119
- Bill type: S
- Bill number: 541
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-12-05T21:54:45Z
- Update date including text: 2025-12-05T21:54:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/541",
    "number": "541",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "ELITE Vehicles Act",
    "type": "S",
    "updateDate": "2025-12-05T21:54:45Z",
    "updateDateIncludingText": "2025-12-05T21:54:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-12",
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
        "item": {
          "date": "2025-02-12T17:53:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "SD"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AR"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "OK"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WY"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ND"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "LA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "KS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ND"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s541is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 541\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Barrasso (for himself, Mr. Thune , Mr. Cotton , Mrs. Capito , Mr. Lankford , Ms. Lummis , Mr. Cramer , Mr. Sheehy , Mr. Ricketts , Ms. Ernst , Mr. Cassidy , Mr. Marshall , Mr. Tillis , Mr. Hoeven , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the credit for new clean vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act .\n#### 2. Repeal of clean vehicle credit\n##### (a) In general\nSubpart B of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 30D (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendments\n**(1)**\nSection 30B(d)(3) of the Internal Revenue Code of 1986 is amended by striking subparagraph (D).\n**(2)**\nSection 38(b) of such Code is amended by striking paragraph (30).\n**(3)**\nSection 179D(d) of such Code is amended\u2014\n**(A)**\nin paragraph (3)(B)(ii), by striking (as defined in section 30D(g)(9)) , and\n**(B)**\nby adding at the end the following new paragraph:\n(6) Indian tribal government For purposes of this subsection, the term Indian tribal government means the recognized governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of this paragraph pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). .\n**(4)**\nSection 1016(a) of such Code is amended\u2014\n**(A)**\nin paragraph (36), by adding and at the end,\n**(B)**\nby striking paragraph (37), and\n**(C)**\nby redesignating paragraph (38) as paragraph (37).\n**(5)**\nSection 6213(g)(2) of such Code is amended by striking subparagraph (T).\n**(6)**\nSection 6417(d)(1)(A)(iv) of such Code is amended by striking section 30D(g)(9) and inserting section 179D(d)(6) .\n**(7)**\nSection 6501(m) of such Code is amended by striking 30D(f)(6), .\n**(8)**\nSection 166(b)(5)(A)(ii) of title 23, United States Code, is amended by inserting , as in effect on the date of the enactment of the ELITE Vehicles Act after section 30D(d)(1) of the Internal Revenue Code of 1986 .\n##### (c) Effective date\nThe amendments made by this section shall apply to vehicles purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.\n#### 3. Repeal of credit for previously-owned clean vehicles\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 25E (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendment\nSection 6213(g)(2) of the Internal Revenue Code of 1986 is amended by striking subparagraph (U).\n##### (c) Effective date\nThe amendments made by this section shall apply to vehicles purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.\n#### 4. Repeal of credit for qualified commercial clean vehicles\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 45W (and by striking the item relating to such section in the table of sections for such subpart).\n##### (b) Conforming amendments\n**(1)**\nSection 38(b) of the Internal Revenue Code of 1986, as amended by sections 13502, 13701, and 13704 of Public Law 117\u2013169 , is amended\u2014\n**(A)**\nby striking paragraph (37), and\n**(B)**\nby redesignating paragraphs (38) through (41) as paragraphs (37) through (40), respectively.\n**(2)**\nSection 6213(g)(2) of such Code is amended\u2014\n**(A)**\nby adding and at the end of subparagraph (R),\n**(B)**\nby striking the comma at the end of subparagraph (S) and inserting a period, and\n**(C)**\nby striking subparagraph (V).\n##### (c) Effective date\nThe amendments made by this section shall apply to vehicles purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.\n#### 5. Exclusion of electric vehicle recharging property from alternative fuel vehicle refueling property credit\n##### (a) In general\nSection 30C of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(B), by striking clause (iii), and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Exclusion of electric vehicle recharging property The term qualified alternative fuel vehicle refueling property shall not include any property for the recharging of motor vehicles propelled by electricity. , and\n**(2)**\nby striking subsection (f).\n##### (b) Effective date\nThe amendments made by this section shall apply to property purchased, or for which a written binding contract to purchase has been entered into, after the date which is 30 days after the date of enactment of this Act.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1367",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ELITE Vehicles Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-05T22:24:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
    "originChamber": "Senate",
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
          "measure-id": "id119s541",
          "measure-number": "541",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s541v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act</strong></p><p>This bill eliminates federal tax credits for the purchase of certain clean vehicles (generally electric vehicles and plug-in hybrid vehicles) and electric\u00a0vehicle recharging stations.</p><p>Specifically, the bill repeals the federal tax credits for</p><ul><li>the purchase of a qualified used clean vehicle (tax credit of up to $4,000 for the purchase of a previously-owned clean vehicle before 2033),</li><li>the purchase of a qualified new clean vehicle (tax credit of up to $7,500 for the purchase of a new clean vehicle before 2033),</li><li>the purchase of a qualified commercial clean vehicle (business tax credit of up to $40,000 for the purchase of a commercial clean vehicle before 2033), and</li><li>alternative fuel vehicle refueling property used to recharge electric vehicles (tax credit of up to $1,000 for individuals or up to $100,000 for businesses for the installation of property before 2033 that is used to recharge electric vehicles).</li></ul>"
        },
        "title": "ELITE Vehicles Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s541.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act</strong></p><p>This bill eliminates federal tax credits for the purchase of certain clean vehicles (generally electric vehicles and plug-in hybrid vehicles) and electric\u00a0vehicle recharging stations.</p><p>Specifically, the bill repeals the federal tax credits for</p><ul><li>the purchase of a qualified used clean vehicle (tax credit of up to $4,000 for the purchase of a previously-owned clean vehicle before 2033),</li><li>the purchase of a qualified new clean vehicle (tax credit of up to $7,500 for the purchase of a new clean vehicle before 2033),</li><li>the purchase of a qualified commercial clean vehicle (business tax credit of up to $40,000 for the purchase of a commercial clean vehicle before 2033), and</li><li>alternative fuel vehicle refueling property used to recharge electric vehicles (tax credit of up to $1,000 for individuals or up to $100,000 for businesses for the installation of property before 2033 that is used to recharge electric vehicles).</li></ul>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s541"
    },
    "title": "ELITE Vehicles Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Eliminate Lavish Incentives To Electric Vehicles Act or the ELITE Vehicles Act</strong></p><p>This bill eliminates federal tax credits for the purchase of certain clean vehicles (generally electric vehicles and plug-in hybrid vehicles) and electric\u00a0vehicle recharging stations.</p><p>Specifically, the bill repeals the federal tax credits for</p><ul><li>the purchase of a qualified used clean vehicle (tax credit of up to $4,000 for the purchase of a previously-owned clean vehicle before 2033),</li><li>the purchase of a qualified new clean vehicle (tax credit of up to $7,500 for the purchase of a new clean vehicle before 2033),</li><li>the purchase of a qualified commercial clean vehicle (business tax credit of up to $40,000 for the purchase of a commercial clean vehicle before 2033), and</li><li>alternative fuel vehicle refueling property used to recharge electric vehicles (tax credit of up to $1,000 for individuals or up to $100,000 for businesses for the installation of property before 2033 that is used to recharge electric vehicles).</li></ul>",
      "updateDate": "2025-09-23",
      "versionCode": "id119s541"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s541is.xml"
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
      "title": "ELITE Vehicles Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ELITE Vehicles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Eliminate Lavish Incentives To Electric Vehicles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to repeal the credit for new clean vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:58Z"
    }
  ]
}
```
