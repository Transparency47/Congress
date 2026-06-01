# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/227?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/227
- Title: PEACE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 227
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-05-27T14:12:50Z
- Update date including text: 2025-05-27T14:12:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/227",
    "number": "227",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "PEACE Act of 2025",
    "type": "S",
    "updateDate": "2025-05-27T14:12:50Z",
    "updateDateIncludingText": "2025-05-27T14:12:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T20:28:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s227is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 227\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Risch (for himself, Mr. Crapo , Mr. Sheehy , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit the use of certain American History and Civics Education program funds for curriculum, or teaching or counseling, that promotes or compels a divisive concept under the priorities noticed in the proposed rule submitted by the Department of Education relating to Proposed Priorities-American History and Civics Education.\n#### 1. Short title\nThis Act may be cited as the Protect Equality And Civics Education Act of 2025 or the PEACE Act of 2025 .\n#### 2. Prohibition on use of funds\nSection 2231 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6661 ) is amended by adding at the end the following:\n(c) Prohibition (1) In General None of the funds made available to carry out this subpart may be used to fund curriculum, or teaching or counseling, that promotes or compels a divisive concept under the priorities noticed in the proposed rule submitted by the Department of Education relating to Proposed Priorities-American History and Civics Education (published at 86 Fed. Reg. 20348 (April 19, 2021)). (2) Definitions In this section: (A) Promotes or compels a divisive concept The term promotes or compels a divisive concept , means race stereotyping or race scapegoating, or promotion of one or more of the following concepts: (i) One race is inherently superior to another race. (ii) The United States is fundamentally racist. (iii) An individual, by virtue of his or her race, is inherently racist or oppressive, whether consciously or unconsciously. (iv) An individual should be discriminated against or receive adverse treatment solely or partly because of his or her race. (v) Members of one race cannot and should not attempt to treat others without respect to race. (vi) An individual's moral character is necessarily determined by his or her race. (vii) An individual, by virtue of his or her race, bears responsibility for actions committed in the past by other members of the same race. (viii) Any individual should feel discomfort, guilt, anguish, or any other form of psychological distress on account of his or her race. (ix) Meritocracy or traits such as a hard work ethic are racist, or were created by a particular race to oppress another race. (B) The term race scapegoating means assigning fault, blame, or bias to a race, or to members of a race because of their race. (C) The term race stereotyping means ascribing character traits, values, moral and ethical codes, privileges, status, or beliefs to a race, or to an individual because of the individual\u2019s race. .",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civics education",
            "updateDate": "2025-03-25T17:27:06Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-25T17:27:00Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-03-25T17:27:21Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-03-25T17:27:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-01T13:14:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s227",
          "measure-number": "227",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s227v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect Equality And Civics Education Act of 2025 or the PEACE Act</strong> <strong>of 2025</strong></p><p>This bill prohibits the use of federal funding made available for the American History and Civics Education program to fund a curriculum, teaching, or counseling that promotes a divisive concept (e.g., race stereotyping or scapegoating) under the priorities noticed in the Department of Education's proposed rule titled <em>Proposed Priorities-American History and Civics Education</em>, published on April 19, 2021.</p>"
        },
        "title": "PEACE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s227.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Equality And Civics Education Act of 2025 or the PEACE Act</strong> <strong>of 2025</strong></p><p>This bill prohibits the use of federal funding made available for the American History and Civics Education program to fund a curriculum, teaching, or counseling that promotes a divisive concept (e.g., race stereotyping or scapegoating) under the priorities noticed in the Department of Education's proposed rule titled <em>Proposed Priorities-American History and Civics Education</em>, published on April 19, 2021.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s227"
    },
    "title": "PEACE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Equality And Civics Education Act of 2025 or the PEACE Act</strong> <strong>of 2025</strong></p><p>This bill prohibits the use of federal funding made available for the American History and Civics Education program to fund a curriculum, teaching, or counseling that promotes a divisive concept (e.g., race stereotyping or scapegoating) under the priorities noticed in the Department of Education's proposed rule titled <em>Proposed Priorities-American History and Civics Education</em>, published on April 19, 2021.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s227"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s227is.xml"
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
      "title": "PEACE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PEACE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Equality And Civics Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of certain American History and Civics Education program funds for curriculum, or teaching or counseling, that promotes or compels a divisive concept under the priorities noticed in the proposed rule submitted by the Department of Education relating to Proposed Priorities-American History and Civics Education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:32Z"
    }
  ]
}
```
