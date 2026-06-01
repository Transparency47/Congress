# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/749
- Title: Stop Illegal Reentry Act
- Congress: 119
- Bill type: HR
- Bill number: 749
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-11-20T09:06:23Z
- Update date including text: 2025-11-20T09:06:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/749",
    "number": "749",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Stop Illegal Reentry Act",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:23Z",
    "updateDateIncludingText": "2025-11-20T09:06:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MT"
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
      "sponsorshipDate": "2025-01-28",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-27",
      "state": "IN"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MT"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TN"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "KS"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr749ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 749\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Bice (for herself, Mr. Zinke , Mrs. Miller of Illinois , and Mr. Hamadeh of Arizona ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to increase penalties for individuals who illegally reenter the United States after being removed, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Stop Illegal Reentry Act .\n#### 2. Increased penalties for reentry of removed alien\nSection 276 of the Immigration and Nationality Act ( 8 U.S.C. 1326 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively;\n**(2)**\nby striking subsections (a) and (b) and inserting the following:\n(a) In general Subject to subsections (b) and (c), any alien who\u2014 (1) has been denied admission, excluded, deported, or removed or has departed the United States while an order of exclusion, deportation, or removal is outstanding; and (2) thereafter enters, attempts to enter, or is at any time found in, the United States, unless\u2014 (A) prior to the alien\u2019s reembarkation at a place outside the United States or the alien\u2019s application for admission from foreign contiguous territory, the Secretary of Homeland Security has expressly consented to such alien\u2019s reapplying for admission; or (B) with respect to an alien previously denied admission and removed, such alien shall establish that the alien was not required to obtain such advance consent under this Act or any prior Act, shall be fined under title 18, United States Code, imprisoned not more than 5 years, or both. (b) Criminal penalties for reentry of certain removed aliens (1) In general Notwithstanding the penalty under subsection (a), and except as provided in subsection (c), an alien described in subsection (a)\u2014 (A) who was convicted before such removal or departure of 3 or more misdemeanors involving drugs, crimes against the person, or both, or a felony (other than an aggravated felony), shall be fined under title 18, United States Code, imprisoned not more than 10 years, or both; (B) who has been excluded from the United States pursuant to section 235(c) because the alien was inadmissible under section 212(a)(3)(B) or who has been removed from the United States pursuant to title V, and who thereafter, without the permission of the Secretary of Homeland Security, enters the United States, or attempts to do so, shall be fined under title 18, United States Code, and imprisoned for a period of 10 years, which sentence shall not run concurrently with any other sentence; (C) who was removed from the United States pursuant to section 241(a)(4)(B) who thereafter, without the permission of the Secretary of Homeland Security, enters, attempts to enter, or is at any time found in, the United States, shall be fined under title 18, United States Code, imprisoned for not more than 10 years, or both; and (D) who has been denied admission, excluded, deported, or removed 3 or more times and thereafter enters, attempts to enter, crosses the border to, attempts to cross the border to, or is at any time found in the United States, shall be fined under title 18, United States Code, imprisoned not more than 10 years, or both. (2) Removal defined In this subsection and in subsection (c), the term removal includes any agreement in which an alien stipulates to removal during (or not during) a criminal trial under either Federal or State law. (c) Mandatory minimum criminal penalty for reentry of certain removed aliens Notwithstanding the penalties provided in subsections (a) and (b), an alien described in subsection (a)\u2014 (1) who was convicted before such removal or departure of an aggravated felony; or (2) who was convicted at least 2 times before such removal or departure of illegal reentry under this section, shall be imprisoned not less than 5 years and not more than 20 years, and may, in addition, be fined under title 18, United States Code. ; and\n**(3)**\nin subsection (d), as redesignated by paragraph (1)\u2014\n**(A)**\nby striking section 242(h)(2) and inserting section 241(a)(4) ; and\n**(B)**\nby striking Attorney General and inserting Secretary of Homeland Security .",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-01-28",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "271",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Illegal Reentry Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-01T17:01:00Z"
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
          "measure-id": "id119hr749",
          "measure-number": "749",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr749v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Illegal Reentry Act</strong></p><p>This bill increases criminal penalties for certain non-U.S. nationals (<em>aliens</em> under federal law) who illegally reenter the United States after removal or exclusion.</p><p>Generally, an individual who had been denied entry into or removed from the United States and who later enters or attempts to enter the United States without prior approval from the Department of Homeland Security shall be fined, imprisoned for up to five years, or both. Current law requires a fine, imprisonment for up to two years, or both, for such an individual.</p><p>An individual who had been denied entry or removed three or more times and who later enters or attempts to enter the United States shall be fined, imprisoned for up to 10 years, or both.</p><p>An individual who was convicted of an aggravated felony or convicted at least two times before removal or departure and who subsequently enters or tries to enter the United States shall be imprisoned at least 5 years and for up to 20 years and may also be fined. Currently, there is no minimum term of imprisonment for an individual who reenters after a conviction for an aggravated felony, and there are no criminal penalties for a reentering individual who had been convicted at least two times (other than the penalties for illegal reentry generally).</p>"
        },
        "title": "Stop Illegal Reentry Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr749.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Illegal Reentry Act</strong></p><p>This bill increases criminal penalties for certain non-U.S. nationals (<em>aliens</em> under federal law) who illegally reenter the United States after removal or exclusion.</p><p>Generally, an individual who had been denied entry into or removed from the United States and who later enters or attempts to enter the United States without prior approval from the Department of Homeland Security shall be fined, imprisoned for up to five years, or both. Current law requires a fine, imprisonment for up to two years, or both, for such an individual.</p><p>An individual who had been denied entry or removed three or more times and who later enters or attempts to enter the United States shall be fined, imprisoned for up to 10 years, or both.</p><p>An individual who was convicted of an aggravated felony or convicted at least two times before removal or departure and who subsequently enters or tries to enter the United States shall be imprisoned at least 5 years and for up to 20 years and may also be fined. Currently, there is no minimum term of imprisonment for an individual who reenters after a conviction for an aggravated felony, and there are no criminal penalties for a reentering individual who had been convicted at least two times (other than the penalties for illegal reentry generally).</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr749"
    },
    "title": "Stop Illegal Reentry Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Illegal Reentry Act</strong></p><p>This bill increases criminal penalties for certain non-U.S. nationals (<em>aliens</em> under federal law) who illegally reenter the United States after removal or exclusion.</p><p>Generally, an individual who had been denied entry into or removed from the United States and who later enters or attempts to enter the United States without prior approval from the Department of Homeland Security shall be fined, imprisoned for up to five years, or both. Current law requires a fine, imprisonment for up to two years, or both, for such an individual.</p><p>An individual who had been denied entry or removed three or more times and who later enters or attempts to enter the United States shall be fined, imprisoned for up to 10 years, or both.</p><p>An individual who was convicted of an aggravated felony or convicted at least two times before removal or departure and who subsequently enters or tries to enter the United States shall be imprisoned at least 5 years and for up to 20 years and may also be fined. Currently, there is no minimum term of imprisonment for an individual who reenters after a conviction for an aggravated felony, and there are no criminal penalties for a reentering individual who had been convicted at least two times (other than the penalties for illegal reentry generally).</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr749"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr749ih.xml"
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
      "title": "Stop Illegal Reentry Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:09Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Illegal Reentry Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to increase penalties for individuals who illegally reenter the United States after being removed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:25Z"
    }
  ]
}
```
