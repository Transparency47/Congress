# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1191
- Title: Commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.
- Congress: 119
- Bill type: HRES
- Bill number: 1191
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-29T18:01:55Z
- Update date including text: 2026-05-29T18:01:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-04-20 - IntroReferral: Submitted in House
- Latest action: 2026-04-20: Submitted in House

## Actions

- 2026-04-20 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-04-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1191",
    "number": "1191",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
    "type": "HRES",
    "updateDate": "2026-05-29T18:01:55Z",
    "updateDateIncludingText": "2026-05-29T18:01:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
          "date": "2026-04-20T16:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1191ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1191\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Crow (for himself, Ms. DeGette , Mr. Neguse , and Ms. Pettersen ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nCommemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.\nThat the House of Representatives\u2014\n**(1)**\ncommemorates the 27th remembrance of the Columbine High School shooting and honors the memories of the victims, survivors, and their families;\n**(2)**\nexpresses heartfelt condolences to all those whose lives were forever altered by the Columbine tragedy;\n**(3)**\ncommemorates the 10th anniversary of the Columbine Day of Service and recognizes community service as a fundamental tool used by the Columbine community and others across the world to rebuild from tragedy and strive for new beginnings;\n**(4)**\nreaffirms the Columbine legacy as one that celebrates the selfless contributions of thousands of students, staff, alumni, first responders, and community members, redefining Columbine beyond the tragic events of April 20, 1999;\n**(5)**\nurges the community to continue its efforts to empower individuals across the world to invest in their communities and to participate in acts of community service; and\n**(6)**\nencourages every United States citizen to remember the victims of the Columbine tragedy, commit to acts of gratitude, and participate annually in the Columbine Day of Service.",
      "versionDate": "2026-04-20",
      "versionType": "IH"
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
        "actionDate": "2026-05-14",
        "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2313)"
      },
      "number": "680",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
      "type": "SRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colorado",
            "updateDate": "2026-05-15T14:59:29Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-05-15T14:59:29Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-05-15T14:59:29Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-05-15T14:59:29Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-05-15T14:59:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-24T19:11:36Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1191ih.xml"
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
      "title": "Commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T08:19:08Z"
    },
    {
      "title": "Commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T08:05:58Z"
    }
  ]
}
```
