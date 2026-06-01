# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4121
- Title: Vote Without Fear Act
- Congress: 119
- Bill type: S
- Bill number: 4121
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-03T15:51:33Z
- Update date including text: 2026-04-03T15:51:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4121",
    "number": "4121",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Vote Without Fear Act",
    "type": "S",
    "updateDate": "2026-04-03T15:51:33Z",
    "updateDateIncludingText": "2026-04-03T15:51:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T21:11:35Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4121is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4121\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Murphy (for himself and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit the unauthorized possession of a firearm at a Federal election site.\n#### 1. Short title\nThis Act may be cited as the Vote Without Fear Act .\n#### 2. Prohibition on unauthorized firearm possession at a Federal election site\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended by adding at the end the following:\n935. Prohibition on unauthorized firearm possession at a Federal election site (a) Definition In this section, the term Federal election site means a building or any part thereof at which an employee of the United States, a State, or a political subdivision thereof is engaged in\u2014 (1) the administration of a polling place in an election for Federal office; or (2) the processing or counting of ballots cast in such an election. (b) Possession of firearm near Federal election site (1) Offense (A) In general Except as provided in subparagraph (B), it shall be unlawful for an individual to knowingly possess or cause to be present a firearm in, or within 100 yards of an entrance to, a place that the individual knows, or has reasonable cause to believe, is a Federal election site. (B) Exceptions Subparagraph (A) shall not apply to\u2014 (i) the possession of a firearm by a law enforcement officer employed by the United States, a State, or a political subdivision thereof, or a private security guard hired or arranged for by the owner or manager of a building in which there is a Federal election site, who is authorized by law to possess a firearm and who is on duty; (ii) the possession of a firearm in a vehicle within 100 yards of an entrance to a Federal election site, if the firearm is not removed from the vehicle or brandished while the vehicle is in, or within 100 yards of the entrance to, the Federal election site; or (iii) the otherwise lawful possession of a firearm in a place of residence, in a place of business, or on private property, in or within 100 yards of an entrance to a Federal election site. (2) Penalty Any individual who violates paragraph (1), or attempts to do so, shall be fined under this title, imprisoned not more than 1 year, or both. (c) Possession of firearm near Federal election site with intent for use in crime (1) Offense It shall be unlawful for an individual, with intent that a firearm be used in the commission of a crime, to knowingly possess or cause to be present the firearm in, or within 100 yards of an entrance to, a place that the individual knows, or has reasonable cause to believe, is a Federal election site. (2) Penalty Any individual who violates paragraph (1), or attempts to do so, shall be fined under this title, imprisoned not more than 5 years, or both. (d) Homicide An individual who kills any other individual in the course of a violation of subsection (b) or (c), or in the course of an attack on a Federal election site involving the use of a firearm, or attempts or conspires to do so, shall be punished as provided in\u2014 (1) section 1111, in the case of murder (as defined in that section); (2) section 1112, in the case of manslaughter (as defined in that section); (3) section 1113, in the case of attempt to commit murder or manslaughter (as those terms are so defined); or (4) section 1117, in the case of conspiracy to commit murder (as so defined). .\n##### (b) Clerical amendment\nThe table of sections for chapter 44 of title 18, United States Code, is amended by adding at the end the following:\n935. Prohibition on unauthorized firearm possession at a Federal election site. .",
      "versionDate": "2026-03-17",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-04-01T17:52:51Z"
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
          "measure-id": "id119s4121",
          "measure-number": "4121",
          "measure-type": "s",
          "orig-publish-date": "2026-03-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4121v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-03-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Vote Without Fear Act</strong></p> <p>This bill establishes new federal criminal offenses for possessing a firearm or causing a firearm to be present in or within 100 yards of a federal election site.<br/> </p>"
        },
        "title": "Vote Without Fear Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4121.xml",
    "summary": {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vote Without Fear Act</strong></p> <p>This bill establishes new federal criminal offenses for possessing a firearm or causing a firearm to be present in or within 100 yards of a federal election site.<br/> </p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s4121"
    },
    "title": "Vote Without Fear Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vote Without Fear Act</strong></p> <p>This bill establishes new federal criminal offenses for possessing a firearm or causing a firearm to be present in or within 100 yards of a federal election site.<br/> </p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s4121"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4121is.xml"
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
      "title": "Vote Without Fear Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Vote Without Fear Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the unauthorized possession of a firearm at a Federal election site.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:37Z"
    }
  ]
}
```
