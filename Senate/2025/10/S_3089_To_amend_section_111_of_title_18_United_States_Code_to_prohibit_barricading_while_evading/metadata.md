# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3089?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3089
- Title: STOP Act
- Congress: 119
- Bill type: S
- Bill number: 3089
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-11-25T20:42:28Z
- Update date including text: 2025-11-25T20:42:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3089",
    "number": "3089",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "STOP Act",
    "type": "S",
    "updateDate": "2025-11-25T20:42:28Z",
    "updateDateIncludingText": "2025-11-25T20:42:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T18:51:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3089is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3089\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 111 of title 18, United States Code, to prohibit barricading while evading arrest.\n#### 1. Short title\nThis Act may be cited as the Secure Takedown and Obstruction Prevention Act or the STOP Act .\n#### 2. Congressional findings\nCongress finds the following:\n**(1)**\nLaw enforcement officers across the United States face unprecedented challenges and dangers in the execution of their duties to protect communities, enforce laws, and maintain public order.\n**(2)**\nBarricading actions often escalate confrontations, prolong dangerous standoffs, divert critical resources, and increase the risk of serious physical harm or death to officers, suspects, and innocent bystanders.\n**(3)**\nFederal law enforcement officers make profound sacrifices every day, including risking their lives to serve and protect the people of the United States. Their unwavering dedication deserves the full support and protection of Federal law.\n#### 3. Offense of barricading during arrest evasion\nSection 111 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Barricading oneself during arrest evasion (1) Definitions In this section: (A) Barricade The term barricade means\u2014 (i) taking a position in a physical location that prevents immediate access by any Federal law enforcement officer; and (ii) refusing and resisting order to exit the location, or comply with other lawful direction, when the person knows or reasonably should know that the Federal law enforcement officer is attempting to apprehend the person. (B) Federal law enforcement officer The term Federal law enforcement officer has the meaning given the term in section 115. (2) Offense It shall be unlawful for any person to\u2014 (A) engage in barricading in the course of forcibly resisting a Federal law enforcement officer engaged in the performance of official duties, in violation of subsection (a)(1); or (B) aid, assist, or attempt to aid or assist another person in committing conduct described in subparagraph (A). (3) Penalty Any person who violates paragraph (2)\u2014 (A) shall be fined under this title, imprisoned for not more than 3 years, or both; or (B) shall be fined under this title, imprisoned for not more than 5 years, or both, if, during the commission of a violation of paragraph (2)\u2014 (i) the violation creates a risk of or causes serious physical harm to any person; (ii) the person has possession or claims possession of a deadly weapon; or (iii) a third party is present and is unable to immediately and safely leave the physical location of the violation. .",
      "versionDate": "2025-10-30",
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
        "updateDate": "2025-11-25T20:42:28Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3089is.xml"
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
      "title": "STOP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure Takedown and Obstruction Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 111 of title 18, United States Code, to prohibit barricading while evading arrest.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T03:48:21Z"
    }
  ]
}
```
