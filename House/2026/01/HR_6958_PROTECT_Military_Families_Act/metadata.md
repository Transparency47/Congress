# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6958?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6958
- Title: PROTECT Military Families Act
- Congress: 119
- Bill type: HR
- Bill number: 6958
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-02-06T14:21:50Z
- Update date including text: 2026-02-06T14:21:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6958",
    "number": "6958",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001123",
        "district": "31",
        "firstName": "Gilbert",
        "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
        "lastName": "Cisneros",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "PROTECT Military Families Act",
    "type": "HR",
    "updateDate": "2026-02-06T14:21:50Z",
    "updateDateIncludingText": "2026-02-06T14:21:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:02:40Z",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6958ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6958\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Mr. Cisneros (for himself and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to require the Secretary of Homeland Security to parole into the United States certain relatives of current and former members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parole Relief Offering Troops Expedited Compassionate Treatment of Military Families Act or as the PROTECT Military Families Act .\n#### 2. Parole for certain relatives of current and former members of the Armed Forces\nSection 212(d)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking subparagraph (B) or and inserting subparagraphs (B) and (C) and ;\n**(2)**\nby striking Attorney General each place such term appears and inserting Secretary of Homeland Security ; and\n**(3)**\nby adding at the end the following:\n(C) (i) Except as provided in clause (iii), the Secretary of Homeland Security shall parole into the United States an alien who is the spouse, widow or widower, parent, or child of\u2014 (I) a member of the Armed Forces on active duty; (II) a member of the Selected Reserve of the Ready Reserve; or (III) an individual, whether living or deceased, who\u2014 (aa) previously served as\u2014 (AA) a member of the Armed Forces on active duty; or (BB) a member of the Selected Reserve of the Ready Reserve; and (bb) was discharged or released from such service under a condition other than dishonorable. (ii) The Secretary of Homeland Security shall parole an alien into the United States under clause (i) in 1-year increments. (iii) (I) An application for parole under this subparagraph may be denied only if the Secretary of Homeland Security, the Secretary of Defense, and the Secretary of Veterans Affairs jointly issue a written justification for the denial. (II) The Secretary of Homeland Security, the Secretary of Defense, and the Secretary of Veterans Affairs may not delegate the responsibility described in subclause (I). (III) (aa) In the case of a denial under subclause (I), the Secretary of Homeland Security shall publish on a publicly available internet website of the Department of Homeland Security information about the denial, including a detailed justification for the denial. (bb) Information published under item (aa) shall not include personally identifiable information. .",
      "versionDate": "2026-01-07",
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
        "actionDate": "2026-01-07",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3592",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PROTECT Military Families Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-22T15:32:30Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6958ih.xml"
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
      "title": "PROTECT Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parole Relief Offering Troops Expedited Compassionate Treatment of Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to require the Secretary of Homeland Security to parole into the United States certain relatives of current and former members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:29Z"
    }
  ]
}
```
