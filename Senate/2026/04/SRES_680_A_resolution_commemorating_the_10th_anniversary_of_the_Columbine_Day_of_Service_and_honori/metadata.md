# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/680
- Title: A resolution commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.
- Congress: 119
- Bill type: SRES
- Bill number: 680
- Origin chamber: Senate
- Introduced date: 2026-04-20
- Update date: 2026-05-29T18:01:56Z
- Update date including text: 2026-05-29T18:01:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in Senate
- 2026-04-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1842)
- 2026-04-20 - IntroReferral: Submitted in Senate
- 2026-05-14 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-14 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2313)
- 2026-05-14 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-05-14 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2026-04-20: Submitted in Senate

## Actions

- 2026-04-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1842)
- 2026-04-20 - IntroReferral: Submitted in Senate
- 2026-05-14 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-14 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2313)
- 2026-05-14 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-05-14 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

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
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/680",
    "number": "680",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "A resolution commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
    "type": "SRES",
    "updateDate": "2026-05-29T18:01:56Z",
    "updateDateIncludingText": "2026-05-29T18:01:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2313)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-14",
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
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1842)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-20",
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
        "item": [
          {
            "date": "2026-05-14T18:29:54Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-20T21:10:22Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres680is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 680\nIN THE SENATE OF THE UNITED STATES\nApril 20, 2026 Mr. Bennet (for himself and Mr. Hickenlooper ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.\nThat the Senate\u2014\n**(1)**\ncommemorates the remembrance of the Columbine High School shooting and honors the memories of the victims, survivors, and their families;\n**(2)**\nexpresses heartfelt condolences to all those whose lives were forever altered by the Columbine tragedy;\n**(3)**\ncommemorates the 10th anniversary of the Columbine Day of Service and recognizes community service as a fundamental tool used by the Columbine community and others across the world to rebuild from tragedy and strive for new beginnings;\n**(4)**\nreaffirms the Columbine legacy as one that celebrates the selfless contributions of thousands of students, staff, alumni, first responders, and community members, redefining Columbine beyond the tragic events of April 20, 1999;\n**(5)**\nurges the community to continue its efforts to empower individuals across the world to invest in their communities and to participate in acts of community service; and\n**(6)**\nencourages every United States citizen to remember the victims of the Columbine tragedy, commit to acts of gratitude, and participate annually in the Columbine Day of Service.",
      "versionDate": "2026-04-20",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres680ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 680\nIN THE SENATE OF THE UNITED STATES\nApril 20, 2026 Mr. Bennet (for himself and Mr. Hickenlooper ) submitted the following resolution; which was referred to the Committee on the Judiciary\nMay 14, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nCommemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.\nThat the Senate\u2014\n**(1)**\ncommemorates the remembrance of the Columbine High School shooting and honors the memories of the victims, survivors, and their families;\n**(2)**\nexpresses heartfelt condolences to all those whose lives were forever altered by the Columbine tragedy;\n**(3)**\ncommemorates the 10th anniversary of the Columbine Day of Service and recognizes community service as a fundamental tool used by the Columbine community and others across the world to rebuild from tragedy and strive for new beginnings;\n**(4)**\nreaffirms the Columbine legacy as one that celebrates the selfless contributions of thousands of students, staff, alumni, first responders, and community members, redefining Columbine beyond the tragic events of April 20, 1999;\n**(5)**\nurges the community to continue its efforts to empower individuals across the world to invest in their communities and to participate in acts of community service; and\n**(6)**\nencourages every United States citizen to remember the victims of the Columbine tragedy, commit to acts of gratitude, and participate annually in the Columbine Day of Service.",
      "versionDate": "2026-05-14",
      "versionType": "ATS"
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
        "actionDate": "2026-04-20",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1191",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
      "type": "HRES"
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
            "updateDate": "2026-05-15T14:59:14Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-05-15T14:59:08Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-05-15T14:58:53Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-05-15T14:59:02Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-05-15T14:58:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-28T15:42:33Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres680is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres680ats.xml"
        }
      ],
      "type": "ATS"
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
      "title": "A resolution commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T03:18:25Z"
    },
    {
      "title": "A resolution commemorating the 10th anniversary of the Columbine Day of Service and honoring the memories of the victims, survivors, and their families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T10:56:23Z"
    }
  ]
}
```
