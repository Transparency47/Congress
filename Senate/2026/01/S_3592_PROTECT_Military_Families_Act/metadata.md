# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3592
- Title: PROTECT Military Families Act
- Congress: 119
- Bill type: S
- Bill number: 3592
- Origin chamber: Senate
- Introduced date: 2026-01-07
- Update date: 2026-02-06T14:21:58Z
- Update date including text: 2026-02-06T14:21:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in Senate
- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-07: Introduced in Senate

## Actions

- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3592",
    "number": "3592",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "PROTECT Military Families Act",
    "type": "S",
    "updateDate": "2026-02-06T14:21:58Z",
    "updateDateIncludingText": "2026-02-06T14:21:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T21:21:22Z",
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
      "sponsorshipDate": "2026-01-07",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "HI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3592is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3592\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2026 Ms. Duckworth (for herself, Mr. Blumenthal , Ms. Hirono , Mr. Wyden , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to require the Secretary of Homeland Security to parole into the United States certain relatives of current and former members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parole Relief Offering Troops Expedited Compassionate Treatment of Military Families Act or PROTECT Military Families Act .\n#### 2. Parole for certain relatives of current and former members of the Armed Forces\nSection 212(d)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking subparagraph (B) or and inserting subparagraphs (B) and (C) and ; and\n**(2)**\nby adding at the end the following:\n(C) (i) Except as provided in clause (iii), the Secretary of Homeland Security shall parole into the United States an alien who is the spouse, widow or widower, parent, or child of\u2014 (I) a member of the Armed Forces on active duty; (II) a member of the Selected Reserve of the Ready Reserve; or (III) an individual, whether living or deceased, who\u2014 (aa) previously served as\u2014 (AA) a member of the Armed Forces on active duty; or (BB) a member of the Selected Reserve of the Ready Reserve; and (bb) was discharged or released from such service under a condition other than dishonorable. (ii) The Secretary of Homeland Security shall parole an alien into the United States under clause (i) in 1-year increments. (iii) (I) An application for parole under this subparagraph may be denied only if the Secretary of Homeland Security, the Secretary of Defense, and the Secretary of Veterans Affairs jointly issue a written justification for the denial. (II) The Secretary of Homeland Security, the Secretary of Defense, and the Secretary of Veterans Affairs may not delegate the responsibility described in subclause (I). (III) (aa) In the case of a denial under subclause (I), the Secretary of Homeland Security shall publish on a publicly available internet website of the Department of Homeland Security information about the denial, including a detailed justification for the denial. (bb) Information published under item (aa) shall not include personally identifiable information. .",
      "versionDate": "2026-01-07",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-01-07",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6958",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PROTECT Military Families Act",
      "type": "HR"
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
        "updateDate": "2026-02-06T14:21:58Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3592is.xml"
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
      "title": "PROTECT Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Parole Relief Offering Troops Expedited Compassionate Treatment of Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to require the Secretary of Homeland Security to parole into the United States certain relatives of current and former members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:28Z"
    }
  ]
}
```
