# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4165
- Title: Educational Visa Transparency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4165
- Origin chamber: Senate
- Introduced date: 2026-03-24
- Update date: 2026-04-03T22:20:46Z
- Update date including text: 2026-04-03T22:20:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in Senate
- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-24: Introduced in Senate

## Actions

- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4165",
    "number": "4165",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Educational Visa Transparency Act of 2026",
    "type": "S",
    "updateDate": "2026-04-03T22:20:46Z",
    "updateDateIncludingText": "2026-04-03T22:20:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:26:12Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4165is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4165\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2026 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require all institutions of higher education receiving Federal assistance to regularly submit information to the Student and Exchange Visitor Information System regarding students, faculty, and administrators who are not United States citizens or lawful permanent residents.\n#### 1. Short title\nThis Act may be cited as the Educational Visa Transparency Act of 2026 .\n#### 2. Mandatory reporting of aliens at institutions of higher education\n##### (a) In general\nSection 641 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1372 ) is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i); and\n**(2)**\nby inserting after subsection (g) the following:\n(h) SEVIS expansion (1) In general Not later than 60 days after the date of the enactment of the Educational Visa Transparency Act of 2026 , and not later than 30 days after each subsequent deadline for class registration for an academic term, each institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )) that receives funding or benefits from the Federal Government shall electronically submit to the Student and Exchange Visitor Information System a complete and accurate list of all students, faculty members, and administrators enrolled at or employed by such institution who are not United States citizens or lawful permanent residents, disaggregated by the type of visa held. (2) Access to information Officials of the Department of Education, the Department of Justice, the Department of Homeland Security, and the Department of State shall have access to the information submitted pursuant to paragraph (1) for the purpose of carrying out the duties of their respective offices. .",
      "versionDate": "2026-03-24",
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
        "name": "Immigration",
        "updateDate": "2026-04-03T22:20:46Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4165is.xml"
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
      "title": "Educational Visa Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Educational Visa Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require all institutions of higher education receiving Federal assistance to regularly submit information to the Student and Exchange Visitor Information System regarding students, faculty, and administrators who are not United States citizens, or lawful permanent residents.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:25Z"
    }
  ]
}
```
