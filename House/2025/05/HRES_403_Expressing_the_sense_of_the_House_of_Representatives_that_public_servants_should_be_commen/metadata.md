# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/403
- Title: Expressing the sense of the House of Representatives that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.
- Congress: 119
- Bill type: HRES
- Bill number: 403
- Origin chamber: House
- Introduced date: 2025-05-09
- Update date: 2025-06-11T14:51:04Z
- Update date including text: 2025-06-11T14:51:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-09: Introduced in House
- 2025-05-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-09 - IntroReferral: Submitted in House
- 2025-05-09 - IntroReferral: Submitted in House
- Latest action: 2025-05-09: Submitted in House

## Actions

- 2025-05-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-09 - IntroReferral: Submitted in House
- 2025-05-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-09",
    "latestAction": {
      "actionDate": "2025-05-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/403",
    "number": "403",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001078",
        "district": "11",
        "firstName": "Gerald",
        "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
        "lastName": "Connolly",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.",
    "type": "HRES",
    "updateDate": "2025-06-11T14:51:04Z",
    "updateDateIncludingText": "2025-06-11T14:51:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-09",
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
          "date": "2025-05-09T17:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "OH"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "TX"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "IL"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "VA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "MA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "VA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "MD"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "MD"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "MD"
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
      "sponsorshipDate": "2025-05-09",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres403ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 403\nIN THE HOUSE OF REPRESENTATIVES\nMay 9, 2025 Mr. Connolly (for himself, Mr. Garcia of California , Mr. Frost , Ms. Brown , Mr. Min , Ms. Crockett , Mr. Krishnamoorthi , Mr. Beyer , Mr. Lynch , Mr. Subramanyam , Ms. McClellan , Mr. Olszewski , Mr. Hoyer , Mr. Mfume , and Ms. Norton ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing the sense of the House of Representatives that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.\nThat the House of Representatives\u2014\n**(1)**\ncommends public servants during Public Service Recognition Week for their outstanding contributions to this great country throughout the year;\n**(2)**\nsalutes government employees and members of the uniformed services for their unyielding dedication to, and enthusiasm for, the public whom they serve;\n**(3)**\nhonors government employees and members of the uniformed services who have given their lives in service to their communities and their country;\n**(4)**\nencourages efforts to promote and celebrate public service careers at every level of government; and\n**(5)**\nexpresses gratitude to the public servants who have selflessly answered the call to serve their country, State, or communities.",
      "versionDate": "2025-05-09",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-11T14:51:04Z"
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
      "date": "2025-05-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres403ih.xml"
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
      "title": "Expressing the sense of the House of Representatives that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T08:18:18Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives that public servants should be commended for their dedication and continued service to the United States during Public Service Recognition Week and throughout the year.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T08:05:42Z"
    }
  ]
}
```
