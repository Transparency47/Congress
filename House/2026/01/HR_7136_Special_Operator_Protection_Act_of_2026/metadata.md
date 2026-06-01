# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7136
- Title: Special Operator Protection Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7136
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-02-10T18:24:25Z
- Update date including text: 2026-02-10T18:24:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7136",
    "number": "7136",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Special Operator Protection Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-10T18:24:25Z",
    "updateDateIncludingText": "2026-02-10T18:24:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
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
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:45Z",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7136ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7136\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Hudson (for himself and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit doxing of special operations personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Special Operator Protection Act of 2026 .\n#### 2. Protection of special operations personnel\n##### (a) In general\nChapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Protection of special operations personnel (a) Definitions In this section: (1) Covered person The term covered person means\u2014 (A) a member of the special operations forces; (B) an employee of the Department of Defense or a member of the Armed Forces (as defined in section 101(a) of title 10) designated by the Secretary of Defense who conducts or participates in Department of Defense sensitive activities (as defined in section 130g of title 10); or (C) a Federal law enforcement officer assigned or attached to, or performing duty with a member of, the special operations forces. (2) Crime of violence The term crime of violence has the meaning given the term in section 16. (3) Immediate family The term immediate family has the meaning given the term in section 115(c). (4) Restricted personal information The term restricted personal information means, with respect to an individual\u2014 (A) the individual\u2019s name in connection with the individual's place of employment; (B) a visual depiction of the individual\u2019s face or likeness in connection with the individual\u2019s name and place of employment; (C) a visual depiction of the individual\u2019s home in connection with the individual\u2019s name and place of employment; (D) the date of birth, Social Security number, home address, home phone number, mobile phone number, personal email, or home fax number of, and identifiable to, the individual; or (E) the individual's biometric data. (b) Offense It shall be unlawful to knowingly make restricted personal information about a covered person, or a member of the immediate family of that covered person, publicly available\u2014 (1) with the intent to threaten, intimidate, or incite the commission of a crime of violence against the covered person or a member of the immediate family of the covered person; or (2) with the intent and knowledge that the restricted personal information will be used to threaten, intimidate, or facilitate the commission of a crime of violence against that covered person or a member of the immediate family of the covered person. (c) Penalties Any person who violates subsection (b)\u2014 (1) shall be fined under this title, imprisoned for not more than 5 years, or both; or (2) if death or serious bodily injury results from the violation, shall be fined under this title, imprisoned for any term of years or for life, or both. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Protection of special operations personnel. .",
      "versionDate": "2026-01-16",
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
        "actionDate": "2026-01-15",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Special Operator Protection Act of 2026",
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
        "updateDate": "2026-02-05T18:39:49Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7136ih.xml"
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
      "title": "Special Operator Protection Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Special Operator Protection Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit doxing of special operations personnel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:40Z"
    }
  ]
}
```
