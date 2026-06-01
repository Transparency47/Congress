# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3803
- Title: Right to Redress Act
- Congress: 119
- Bill type: S
- Bill number: 3803
- Origin chamber: Senate
- Introduced date: 2026-02-09
- Update date: 2026-03-03T16:03:56Z
- Update date including text: 2026-03-03T16:03:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in Senate
- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-09: Introduced in Senate

## Actions

- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3803",
    "number": "3803",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Right to Redress Act",
    "type": "S",
    "updateDate": "2026-03-03T16:03:56Z",
    "updateDateIncludingText": "2026-03-03T16:03:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T21:01:32Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3803is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3803\nIN THE SENATE OF THE UNITED STATES\nFebruary 9, 2026 Mr. Booker (for himself, Mr. Blumenthal , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to permit actions to be instituted upon claims against the United States for money damages for personal injuries and death caused by Federal law enforcement officers without first being presented to the appropriate Federal agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right to Redress Act .\n#### 2. Tort claims procedure\n##### (a) In general\nChapter 171 of title 28, United States Code, is amended\u2014\n**(1)**\nin section 2675 of title 28, United States Code, is amended\u2014\n**(A)**\nin subsection (a), in the third sentence, by inserting claims against the United States for money damages for injury or loss of property or personal injury or death caused by the negligent or wrongful act or omission of any Federal law enforcement officer while acting within the scope of the office or employment of the officer or before such claims ; and\n**(B)**\nby adding at the end the following:\n(d) Any claim against the United States for money damages for injury or loss of property or personal injury or death caused by the negligent or wrongful act or omission of any Federal law enforcement officer while acting within the scope of the office or employment of the officer shall, at the request of the claimant, be tried by the court with a jury. (e) In this section, the term Federal law enforcement officer means any officer, agent, or employee of the United States authorized by law or by a Government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of Federal civil or criminal law. ;\n**(2)**\nin section 2676, by striking The and inserting Except with regard to acts or omissions of Federal law enforcement officers described in section 2675(a), the ; and\n**(3)**\nin section 2680\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (a) Any and inserting (a)(1) Except as provided in paragraph (2), any ; and\n**(ii)**\nby adding at the end the following:\n(2) With regard to acts or omissions of Federal law enforcement officers described in section 2675(a), the provisions of this chapter and section 1346(b) of this title shall apply to any claim described in paragraph (1). ; and\n**(B)**\nin subsection (h), in the second sentence, by striking means and all that follows through the end and inserting has the meaning given the term Federal law enforcement officer in section 2675(e). .\n##### (b) Technical and conforming amendment\nSection 2402 of title 28, United States Code, is amended by inserting section 2675(d) and before chapter 179 .\n##### (c) Applicability\nThe amendments made by subsections (a) and (b) shall apply to any claim arising before, on, or after the date of enactment of this Act.\n##### (d) Rule of construction\nNothing in this section, or the amendments made by this section, may be construed to\u2014\n**(1)**\nrevive any claim for which the applicable statute of limitations has expired; or\n**(2)**\nreopen any claim that has been finally adjudicated, whether administratively or by a Federal court.",
      "versionDate": "2026-02-09",
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
        "name": "Law",
        "updateDate": "2026-03-03T16:03:56Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3803is.xml"
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
      "title": "Right to Redress Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T07:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Right to Redress Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T07:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 28, United States Code, to permit actions to be instituted upon claims against the United States for money damages for personal injuries and death caused by Federal law enforcement officers without first being presented to the appropriate Federal agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T07:18:16Z"
    }
  ]
}
```
