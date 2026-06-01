# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/36?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/36
- Title: Finding Federal Savings Committee Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 36
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-02-07T01:24:54Z
- Update date including text: 2025-02-07T01:24:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-13 - Committee: Submitted in House
- 2025-01-13 - IntroReferral: Submitted in House
- Latest action: 2025-01-13: Submitted in House

## Actions

- 2025-01-13 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-13 - Committee: Submitted in House
- 2025-01-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/36",
    "number": "36",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Finding Federal Savings Committee Resolution",
    "type": "HRES",
    "updateDate": "2025-02-07T01:24:54Z",
    "updateDateIncludingText": "2025-02-07T01:24:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-13T17:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "IN"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres36ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 36\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Obernolte (for himself, Mr. Weber of Texas , Mr. Webster of Florida , Ms. Tenney , and Mr. Valadao ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to establish the Committee on the Elimination of Nonessential Federal Programs.\n#### 1. Short title\nThis resolution may be cited as the Finding Federal Savings Committee Resolution .\n#### 2. Committee on the Elimination of Nonessential Federal Programs\n##### (a)\nClause 1 of rule X of the Rules of the House of Representatives is amended by redesignating paragraphs (f) through (t) as paragraphs (g) through (u) and by inserting after paragraph (e) the following new paragraph:\n(f) Elimination of Nonessential Federal Programs Modification or elimination of underperforming or nonessential Federal programs. The committee shall cease to exist at the close of the 120th Congress. .\n##### (b)\nClause 4 of rule X of the Rules of the House of Representatives is amended by adding at the end the following new paragraph:\n(g) The Committee on the Elimination of Nonessential Federal Programs shall\u2014 (1) (A) research, review, and study Federal programs that are underperforming or nonessential; and (B) determine which Federal programs should be modified or eliminated; (2) develop recommendations to the House for action designed to modify or eliminate underperforming or nonessential Federal programs; and (3) submit to the House\u2014 (A) at least once a year, reports including\u2014 (i) a detailed statement of the findings and conclusions of the Committee; and (ii) a list of underperforming or nonessential Federal programs; and (B) legislation to eliminate the programs described in section subdivision (ii) and rescissions based on the findings of the report described in subdivision (i). .\n##### (c)\nClause 5(a) of rule X of the Rules of the House of Representatives is amended by adding at the end the following new paragraph:\n(4) (A) The Committee on the Elimination of Nonessential Federal Programs shall be composed of members as follows: (i) Four members from the Committee on Appropriations. (ii) Four members from the Committee on the Budget. (iii) Four members from the Committee on Oversight and Government Reform. (iv) Four members from the Committee on Ways and Means. (v) One member who does not serve on any of committees described in items (i) through (iv), who shall be appointed by the Speaker and designated by the Speaker as the Chair of the Committee. (vi) One member who does not serve on any of committees described in items (i) through (iv), who shall be appointed by the minority leader and designated by the minority leader as the Vice Chair of the Committee. (B) The Chair and Vice Chair of the Committee shall not be from the same political party. (C) Of the members appointed from each of the four committees listed in subdivision (A), two shall be from the minority party. .\n##### (d)\nRule X of the Rules of the House of Representatives is amended by adding at the end the following new clause:\nExpedited procedures for legislation reported by the Committee on the Elimination of Nonessential Federal Programs 12. With respect to any bill or resolution reported by the Committee on the Elimination of Nonessential Federal Programs, the following shall apply: (a) After the expiration of the 7-day period (excluding any day on which the House is not in session) that begins on the date the Committee reports the bill or resolution, it is in order to move to proceed to the consideration of the bill or resolution. The motion is highly privileged and is not debatable, an amendment to the motion is not in order, and it is not in order to move to reconsider the vote by which the motion is agreed to or disagreed to. (b) Debate on the bill or resolution shall be limited to not more than 10 hours, which shall be divided equally between those favoring and those opposing the bill or resolution. A motion to further limit debate is not debatable. (c) An amendment to, or motion to recommit, the bill or resolution is not in order, and it is not in order to move to reconsider the vote by which the bill or resolution is agreed to or disagreed to. .",
      "versionDate": "2025-01-13",
      "versionType": "IH"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional committees",
            "updateDate": "2025-01-15T18:40:57Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-01-15T18:41:03Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:41:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-14T18:20:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hres36",
          "measure-number": "36",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres36v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Finding Federal Savings Committee Resolution</strong></p> <p>This resolution establishes the House Committee on the Elimination of Nonessential Federal Programs to analyze underperforming or nonessential federal programs and recommend actions to modify or eliminate those programs. The resolution also establishes expedited procedures for legislation reported by the committee to eliminate programs or rescind funding.</p> <p>The committee shall cease to exist at the end of the 120th Congress.</p>"
        },
        "title": "Finding Federal Savings Committee Resolution"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres36.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Finding Federal Savings Committee Resolution</strong></p> <p>This resolution establishes the House Committee on the Elimination of Nonessential Federal Programs to analyze underperforming or nonessential federal programs and recommend actions to modify or eliminate those programs. The resolution also establishes expedited procedures for legislation reported by the committee to eliminate programs or rescind funding.</p> <p>The committee shall cease to exist at the end of the 120th Congress.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres36"
    },
    "title": "Finding Federal Savings Committee Resolution"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Finding Federal Savings Committee Resolution</strong></p> <p>This resolution establishes the House Committee on the Elimination of Nonessential Federal Programs to analyze underperforming or nonessential federal programs and recommend actions to modify or eliminate those programs. The resolution also establishes expedited procedures for legislation reported by the committee to eliminate programs or rescind funding.</p> <p>The committee shall cease to exist at the end of the 120th Congress.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres36"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres36ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Finding Federal Savings Committee Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-14T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Finding Federal Savings Committee Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-14T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amending the Rules of the House of Representatives to establish the Committee on the Elimination of Nonessential Federal Programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-14T09:33:17Z"
    }
  ]
}
```
