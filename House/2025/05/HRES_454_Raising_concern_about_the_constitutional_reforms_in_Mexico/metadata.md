# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/454
- Title: Raising concern about the constitutional reforms in Mexico.
- Congress: 119
- Bill type: HRES
- Bill number: 454
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-06-20T13:18:31Z
- Update date including text: 2025-06-20T13:18:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House
- Latest action: 2025-05-29: Submitted in House

## Actions

- 2025-05-29 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/454",
    "number": "454",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Raising concern about the constitutional reforms in Mexico.",
    "type": "HRES",
    "updateDate": "2025-06-20T13:18:31Z",
    "updateDateIncludingText": "2025-06-20T13:18:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-29T15:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres454ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 454\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Stanton (for himself and Ms. Salazar ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRaising concern about the constitutional reforms in Mexico.\nThat the House of Representatives\u2014\n**(1)**\nraises concern that the constitutional reforms and secondary legislation would have a long-term negative impact on Mexico\u2019s democratic institutions, separation of powers, judicial independence and transparency, and security, while undermining its electoral system, National Guard, and independent oversight agencies;\n**(2)**\nexpresses deep concern that the constitutional reforms and secondary legislation may contradict commitments made in the United States-Mexico-Canada Trade Agreement, jeopardizing critical economic and security interests shared by the United States and Mexico and weakening North American economic integration;\n**(3)**\nunderscores that several aspects of the reform package undermine United States-Mexico joint efforts to strengthen the rule of law, counter organized crime, and address the scourge of fentanyl and human and arms trafficking among broader bilateral priorities; and\n**(4)**\nreaffirms its commitment to a robust, mutually respectful relationship between the sovereign countries of the United States and Mexico.",
      "versionDate": "2025-05-29",
      "versionType": "IH"
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
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:18:31Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres454ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Raising concern about the constitutional reforms in Mexico.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T09:18:16Z"
    },
    {
      "title": "Raising concern about the constitutional reforms in Mexico.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T08:05:32Z"
    }
  ]
}
```
