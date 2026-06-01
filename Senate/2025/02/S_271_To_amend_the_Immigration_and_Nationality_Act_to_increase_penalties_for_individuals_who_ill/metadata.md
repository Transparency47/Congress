# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/271?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/271
- Title: Stop Illegal Reentry Act
- Congress: 119
- Bill type: S
- Bill number: 271
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/271",
    "number": "271",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop Illegal Reentry Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T19:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "IA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "OK"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MS"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s271is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 271\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Cruz (for himself, Mr. Scott of Florida , Mr. Grassley , Mr. Lankford , Mr. Budd , Mr. Justice , Mr. Ricketts , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to increase penalties for individuals who illegally reenter the United States after being removed, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Illegal Reentry Act .\n#### 2. Increased penalties for reentry of removed alien\nSection 276 of the Immigration and Nationality Act ( 8 U.S.C. 1326 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (e) and (f), respectively;\n**(2)**\nby striking subsections (a) and (b) and inserting the following:\n(a) Defined term In this section, the term removal includes any agreement in which an alien stipulates to removal during (or not during) a criminal trial under either Federal or State law. (b) In general Subject to subsections (c) and (d), any alien who\u2014 (1) has been denied admission, excluded, deported, or removed or has departed the United States while an order of exclusion, deportation, or removal is outstanding; and (2) thereafter enters, attempts to enter, or is at any time found in, the United States, unless\u2014 (A) prior to the alien\u2019s reembarkation at a place outside the United States or the alien\u2019s application for admission from foreign contiguous territory, the Secretary of Homeland Security has expressly consented to such alien\u2019s reapplying for admission; or (B) with respect to an alien previously denied admission and removed, such alien shall establish that the alien was not required to obtain such advance consent under this Act or any prior Act, shall be fined under title 18, United States Code, imprisoned not more than 5 years, or both. (c) Criminal penalties for reentry of certain removed aliens (1) In general Notwithstanding the penalty under subsection (b), and except as provided in subsection (d), an alien described in subsection (b)\u2014 (A) who was convicted before such removal or departure of 3 or more misdemeanors involving drugs, crimes against the person, or both, or a felony (other than an aggravated felony), shall be fined under title 18, United States Code, imprisoned not more than 10 years, or both; (B) who has been excluded from the United States pursuant to section 235(c) because the alien was inadmissible under section 212(a)(3)(B) or who has been removed from the United States pursuant to title V, and who thereafter, without the permission of the Secretary of Homeland Security, enters the United States, or attempts to do so, shall be fined under title 18, United States Code, and imprisoned for a period of 10 years, which sentence shall not run concurrently with any other sentence; (C) who was removed from the United States pursuant to section 241(a)(4)(B) who thereafter, without the permission of the Secretary of Homeland Security, enters, attempts to enter, or is at any time found in, the United States, shall be fined under title 18, United States Code, imprisoned for not more than 10 years, or both; and (D) who has been denied admission, excluded, deported, or removed 3 or more times and thereafter enters, attempts to enter, crosses the border to, attempts to cross the border to, or is at any time found in the United States, shall be fined under title 18, United States Code, imprisoned not more than 10 years, or both. (d) Mandatory minimum criminal penalty for reentry of certain removed aliens Notwithstanding the penalties provided in subsections (b) and (c), an alien described in subsection (b)\u2014 (1) who was convicted before such removal or departure of an aggravated felony; or (2) who was convicted at least twice before such removal or departure of illegal reentry under this section, shall be imprisoned not less than 5 years and not more than 20 years, and may, in addition, be fined under title 18, United States Code. ;\n**(3)**\nin subsection (e), as redesignated\u2014\n**(A)**\nby striking section 242(h)(2) and inserting section 241(a)(4) ; and\n**(B)**\nby striking Attorney General and inserting Secretary of Homeland Security ; and\n**(4)**\nin subsection (f), as redesignated, in the matter preceding paragraph (1), by striking subsection (a)(1) or subsection (b) and inserting subsection (b)(1) or (c) .",
      "versionDate": "2025-02-28",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "749",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Illegal Reentry Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-06T16:19:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119s271",
          "measure-number": "271",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s271v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Illegal Reentry Act</strong></p><p>This bill increases criminal penalties for certain non-U.S. nationals (<em>aliens</em> under federal law) who illegally reenter the United States after removal or exclusion.</p><p>Generally, an individual who had been denied entry into or removed from the United States and who later enters or attempts to enter the United States without prior approval from the Department of Homeland Security shall be fined, imprisoned for up to five years, or both. Current law requires a fine, imprisonment for up to two years, or both, for such an individual.</p><p>An individual who had been denied entry or removed three or more times and who later enters or attempts to enter the United States shall be fined, imprisoned for up to 10 years, or both.</p><p>An individual who was convicted of an aggravated felony or convicted at least two times before removal or departure and who subsequently enters or tries to enter the United States shall be imprisoned at least 5 years and for up to 20 years and may also be fined. Currently, there is no minimum term of imprisonment for an individual who reenters after a conviction for an aggravated felony, and there are no criminal penalties for a reentering individual who had been convicted at least two times (other than the penalties for illegal reentry generally).</p>"
        },
        "title": "Stop Illegal Reentry Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s271.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Illegal Reentry Act</strong></p><p>This bill increases criminal penalties for certain non-U.S. nationals (<em>aliens</em> under federal law) who illegally reenter the United States after removal or exclusion.</p><p>Generally, an individual who had been denied entry into or removed from the United States and who later enters or attempts to enter the United States without prior approval from the Department of Homeland Security shall be fined, imprisoned for up to five years, or both. Current law requires a fine, imprisonment for up to two years, or both, for such an individual.</p><p>An individual who had been denied entry or removed three or more times and who later enters or attempts to enter the United States shall be fined, imprisoned for up to 10 years, or both.</p><p>An individual who was convicted of an aggravated felony or convicted at least two times before removal or departure and who subsequently enters or tries to enter the United States shall be imprisoned at least 5 years and for up to 20 years and may also be fined. Currently, there is no minimum term of imprisonment for an individual who reenters after a conviction for an aggravated felony, and there are no criminal penalties for a reentering individual who had been convicted at least two times (other than the penalties for illegal reentry generally).</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s271"
    },
    "title": "Stop Illegal Reentry Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Illegal Reentry Act</strong></p><p>This bill increases criminal penalties for certain non-U.S. nationals (<em>aliens</em> under federal law) who illegally reenter the United States after removal or exclusion.</p><p>Generally, an individual who had been denied entry into or removed from the United States and who later enters or attempts to enter the United States without prior approval from the Department of Homeland Security shall be fined, imprisoned for up to five years, or both. Current law requires a fine, imprisonment for up to two years, or both, for such an individual.</p><p>An individual who had been denied entry or removed three or more times and who later enters or attempts to enter the United States shall be fined, imprisoned for up to 10 years, or both.</p><p>An individual who was convicted of an aggravated felony or convicted at least two times before removal or departure and who subsequently enters or tries to enter the United States shall be imprisoned at least 5 years and for up to 20 years and may also be fined. Currently, there is no minimum term of imprisonment for an individual who reenters after a conviction for an aggravated felony, and there are no criminal penalties for a reentering individual who had been convicted at least two times (other than the penalties for illegal reentry generally).</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s271"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s271is.xml"
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
      "title": "Stop Illegal Reentry Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Illegal Reentry Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to increase penalties for individuals who illegally reenter the United States after being removed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:27Z"
    }
  ]
}
```
