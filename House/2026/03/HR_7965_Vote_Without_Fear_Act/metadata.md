# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7965?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7965
- Title: Vote Without Fear Act
- Congress: 119
- Bill type: HR
- Bill number: 7965
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-05-14T08:08:09Z
- Update date including text: 2026-05-14T08:08:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7965",
    "number": "7965",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Vote Without Fear Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:09Z",
    "updateDateIncludingText": "2026-05-14T08:08:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T14:02:20Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "DC"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "RI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7965ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7965\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Mr. Ruiz (for himself and Ms. Norton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the unauthorized possession of a firearm at a Federal election site.\n#### 1. Short title\nThis Act may be cited as the Vote Without Fear Act .\n#### 2. Prohibition on unauthorized firearm possession at a Federal election site\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended by adding at the end the following:\n935. Prohibition on unauthorized firearm possession at a Federal election site (a) (1) Except as provided in paragraph (2), whoever knowingly possesses or causes to be present a firearm in, or within 100 yards of an entrance to, a place that the individual knows, or has reasonable cause to believe, is a Federal election site, or attempts to do so, shall be fined under this title, imprisoned not more than 1 year, or both. (2) Paragraph (1) shall not apply to\u2014 (A) the possession of a firearm by a law enforcement officer employed by the United States, a State, or a political subdivision thereof, or a private security guard hired or arranged for by the owner or manager of a building in which there is a Federal election site, who is authorized by law to possess a firearm and who is on duty; (B) the possession of a firearm in a vehicle within 100 yards of an entrance to a Federal election site, if the firearm is not removed from the vehicle or brandished while the vehicle is in, or within 100 yards of the entrance to, the Federal election site; or (C) the otherwise lawful possession of a firearm in a place of residence, in a place of business, or on private property, in or within 100 yards of an entrance to a Federal election site. (b) Whoever, with intent that a firearm be used in the commission of a crime, knowingly possesses or causes to be present the firearm in, or within 100 yards of an entrance to, a place that the individual knows, or has reasonable cause to believe, is a Federal election site, or attempts to do so, shall be fined under this title, imprisoned not more than 5 years, or both. (c) A person who kills any person in the course of a violation of subsection (a) or (b), or in the course of an attack on a Federal election site, involving the use of a firearm, or attempts or conspires to do so, shall be punished as provided in sections 1111, 1112, 1113, and 1117. (d) In this section, the term Federal election site means a building or any part thereof at which an employee of the United States, a State, or a political subdivision thereof is engaged in\u2014 (1) the administration of a polling place in an election for Federal office; or (2) the processing or counting of ballots cast in such an election. .\n##### (b) Clerical amendment\nThe table of sections for such chapter is amended by adding at the end the following new item:\n935. Prohibition on unauthorized firearm possession at a Federal election site. .",
      "versionDate": "2026-03-17",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-02T16:49:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-17",
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
          "measure-id": "id119hr7965",
          "measure-number": "7965",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7965v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-03-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Vote Without Fear Act</strong></p> <p>This bill establishes new federal criminal offenses for possessing a firearm or causing a firearm to be present in or within 100 yards of a federal election site.<br/> </p>"
        },
        "title": "Vote Without Fear Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7965.xml",
    "summary": {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Vote Without Fear Act</strong></p> <p>This bill establishes new federal criminal offenses for possessing a firearm or causing a firearm to be present in or within 100 yards of a federal election site.<br/> </p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr7965"
    },
    "title": "Vote Without Fear Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Vote Without Fear Act</strong></p> <p>This bill establishes new federal criminal offenses for possessing a firearm or causing a firearm to be present in or within 100 yards of a federal election site.<br/> </p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr7965"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7965ih.xml"
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
      "title": "Vote Without Fear Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vote Without Fear Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the unauthorized possession of a firearm at a Federal election site.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T07:48:38Z"
    }
  ]
}
```
