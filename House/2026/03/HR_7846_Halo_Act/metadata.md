# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7846?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7846
- Title: Halo Act
- Congress: 119
- Bill type: HR
- Bill number: 7846
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-13T08:06:42Z
- Update date including text: 2026-05-13T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7846",
    "number": "7846",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Halo Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:42Z",
    "updateDateIncludingText": "2026-05-13T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:05:45Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "ID"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7846ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7846\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Rulli (for himself, Mr. Moore of Alabama , Mr. Simpson , and Mr. Fine ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish a criminal penalty for obstructing immigration enforcement activities.\n#### 1. Short title\nThis Act may be cited as the Halo Act .\n#### 2. Criminal penalty for obstructing immigration enforcement activities\n##### (a) In general\nChapter 73 of title 18, United States Code, is amended by adding at the end the following:\n1522. Obstructing immigration enforcement activities (a) Definitions In this section: (1) Federal immigration enforcement officer The term Federal immigration enforcement officer means any officer, agent, or employee of the United States authorized by law or by a government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of Federal immigration law. (2) Harass The term harass means to knowingly engage in a course of conduct directed at a Federal immigration enforcement officer that intentionally causes substantial emotional distress in that Federal immigration enforcement officer and serves no legitimate purpose. (b) Offense It shall be unlawful for a person, after receiving a verbal warning not to approach from an individual whom the person knows or reasonably should know is a Federal immigration enforcement officer, and who is engaged in the lawful performance of a legal duty, to knowingly violate the warning and approach or remain within 25 feet of the Federal immigration enforcement officer with the intent to\u2014 (1) impede or interfere with the ability of the Federal immigration enforcement officer to perform that legal duty; (2) threaten the Federal immigration enforcement officer with physical harm; or (3) harass the Federal immigration enforcement officer. (c) Penalty Any person who violates subsection (b) shall be fined under this title, imprisoned for not more than 5 years, or both. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 73 of title 18, United States Code, is amended by adding at the end the following:\n1522. Obstructing immigration enforcement activities. .",
      "versionDate": "2026-03-05",
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3179",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Halo Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-01T16:35:44Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7846ih.xml"
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
      "title": "Halo Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Halo Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish a criminal penalty for obstructing immigration enforcement activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:24Z"
    }
  ]
}
```
