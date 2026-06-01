# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8240?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8240
- Title: SAFER Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8240
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-14T19:24:02Z
- Update date including text: 2026-04-14T19:24:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8240",
    "number": "8240",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000165",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
        "lastName": "Tiffany",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "SAFER Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-14T19:24:02Z",
    "updateDateIncludingText": "2026-04-14T19:24:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:33:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8240ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8240\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Tiffany introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to prohibit return to a county of concern with an asylum application.\n#### 1. Short title\nThis Act may be cited as the Stopping Asylum Fraudsters Enforcement and Removal Act of 2026 or the SAFER Act of 2026 .\n#### 2. Prohibition on return to country of concern for asylum applications\nSection 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ) is amended by adding at the end the following:\n(f) Prohibition on return to country of concern (1) Prohibition The Secretary of Homeland Security or the Attorney General may not grant asylum to an alien who has returned to a country of concern. (2) Effect on status An alien who has been granted asylum and returns to a country of concern shall be subject to termination of a grant of asylum, denaturalization, and is subject to any applicable grounds of inadmissibility or deportability under section 212(a) and 237(a). (3) Exception Paragraphs (1) and (2) may be waived by the Secretary of Homeland Security or the Attorney General, as applicable, on a case-by-case basis if\u2014 (A) the President certifies that the individual is permitted to travel for national security purposes; or (B) the Secretary of State certifies that the country of concern has undergone a legitimate transfer of power. (4) Country of concern defined In this section, the term country of concern means the alien's country of nationality or, in the case of a person having no nationality, the country of the alien's last habitual residence for which the alien applied for asylum pursuant to this section. .",
      "versionDate": "2026-04-09",
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
        "name": "Immigration",
        "updateDate": "2026-04-14T19:24:01Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8240ih.xml"
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
      "title": "SAFER Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFER Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Asylum Fraudsters Enforcement and Removal Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to prohibit return to a county of concern with an asylum application.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:39Z"
    }
  ]
}
```
