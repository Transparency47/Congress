# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/662?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/662
- Title: A resolution honoring the life and service of United States Marine Corps veteran Nicholas Douglas Quets, expressing condolences to his family, and condemning cartel violence.
- Congress: 119
- Bill type: SRES
- Bill number: 662
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-02T22:22:37Z
- Update date including text: 2026-04-02T22:22:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1673-1674)
- 2026-03-26 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-26: Submitted in Senate

## Actions

- 2026-03-26 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1673-1674)
- 2026-03-26 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/662",
    "number": "662",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A resolution honoring the life and service of United States Marine Corps veteran Nicholas Douglas Quets, expressing condolences to his family, and condemning cartel violence.",
    "type": "SRES",
    "updateDate": "2026-04-02T22:22:37Z",
    "updateDateIncludingText": "2026-04-02T22:22:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1673-1674)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-03-26T22:57:42Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres662is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 662\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Kelly submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the life and service of United States Marine Corps veteran Nicholas Douglas Quets, expressing condolences to his family, and condemning cartel violence.\nThat the Senate\u2014\n**(1)**\nhonors the life, service, and memory of United States Marine Corps veteran Nicholas Douglas Quets;\n**(2)**\nexpresses its deepest condolences to the family, friends, and loved ones of Nicholas Quets;\n**(3)**\ncondemns the violent actions of the Sinaloa Cartel and other transnational criminal organizations responsible for acts of brutality that endanger innocent lives;\n**(4)**\nrecognizes the broader threat posed by cartel violence to regional stability and the safety of United States citizens; and\n**(5)**\nreaffirms the commitment of the United States to pursuing justice and combating transnational criminal organizations that threaten peace, security, and the rule of law.",
      "versionDate": "2026-03-26",
      "versionType": "IS"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-02T22:22:37Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres662is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution honoring the life and service of United States Marine Corps veteran Nicholas Douglas Quets, expressing condolences to his family, and condemning cartel violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T06:18:26Z"
    },
    {
      "title": "A resolution honoring the life and service of United States Marine Corps veteran Nicholas Douglas Quets, expressing condolences to his family, and condemning cartel violence.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T10:56:21Z"
    }
  ]
}
```
