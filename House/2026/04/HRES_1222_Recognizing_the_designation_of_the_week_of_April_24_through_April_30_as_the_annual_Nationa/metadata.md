# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1222
- Title: Recognizing the designation of the week of April 24 through April 30 as the annual "National Reentry Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1222
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-06T19:58:19Z
- Update date including text: 2026-05-06T19:58:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-04-28 - IntroReferral: Submitted in House
- Latest action: 2026-04-28: Submitted in House

## Actions

- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-04-28 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1222",
    "number": "1222",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the designation of the week of April 24 through April 30 as the annual \"National Reentry Week\".",
    "type": "HRES",
    "updateDate": "2026-05-06T19:58:19Z",
    "updateDateIncludingText": "2026-05-06T19:58:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
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
      "actionCode": "1025",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
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
          "date": "2026-04-28T13:03:10Z",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "OH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "DC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "TN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1222ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1222\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Ms. Kamlager-Dove (for herself, Mrs. McIver , Ms. Vel\u00e1zquez , Mrs. Beatty , Mr. Johnson of Georgia , Ms. Tlaib , Ms. Norton , Mr. Jackson of Illinois , Ms. Simon , Mr. Davis of Illinois , Mr. Cohen , and Mr. Thanedar ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the designation of the week of April 24 through April 30 as the annual National Reentry Week .\nThat the House of Representatives recognizes\u2014\n**(1)**\nthe annual National Reentry Week ; and\n**(2)**\nthat\u2014\n**(A)**\nthe United States is experiencing a mass incarceration crisis with mass incarceration rates increasing by 500 percent since 1970, and mass incarceration and cycles of structural marginalization have created dangerously high rates of recidivism;\n**(B)**\nthe Nation has a responsibility to advance reentry programs that promote opportunity, bolster public safety, and grant formerly incarcerated individuals the opportunity to reenter communities with financial and mental stability;\n**(C)**\nto better mitigate high recidivism rates, Congress must work toward addressing existing obstacles to successful reentry by increasing access for formerly incarcerated individuals to\u2014\n**(i)**\nhalfway homes and housing resources upon release;\n**(ii)**\neducation programs while incarcerated;\n**(iii)**\nopportunities for higher education grants following their release;\n**(iv)**\noccupational training opportunities while incarcerated; and\n**(v)**\naccess to mental health services;\n**(D)**\nto improve reentry outcomes for the formerly incarcerated, Congress must invest in criminal justice frameworks that address high rates of recidivism and support the individual success and rights of incarcerated individuals before and after reentry;\n**(E)**\nincarcerated persons must have access to resources and programs that encourage their successful reentry; and\n**(F)**\nNational Reentry Week is an opportunity\u2014\n**(i)**\nto deepen the national conversation about recidivism in the United States;\n**(ii)**\nto amplify and invest in community-driven policy, research, and recidivism solutions;\n**(iii)**\nto improve the outcomes of incarcerated persons upon reentry into society;\n**(iv)**\nto provide a national platform for entities centered on formerly incarcerated persons and their efforts to ensure the successful reentry of formerly incarcerated persons into society;\n**(v)**\nto support efforts to increase funding and advance policies for organizations that provide housing, occupational training, and mental health resources for incarcerated persons reentering society; and\n**(vi)**\nto invest in evidence-based policy solutions to create safer communities across the Nation.",
      "versionDate": "2026-04-28",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-06T19:58:19Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1222ih.xml"
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
      "title": "Recognizing the designation of the week of April 24 through April 30 as the annual \"National Reentry Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T08:18:46Z"
    },
    {
      "title": "Recognizing the designation of the week of April 24 through April 30 as the annual \"National Reentry Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T08:07:03Z"
    }
  ]
}
```
