# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/124
- Title: A resolution recognizing the 250th anniversary of the United States Marine Corps.
- Congress: 119
- Bill type: SRES
- Bill number: 124
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-03-12T15:09:46Z
- Update date including text: 2026-03-12T15:09:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1716)
- 2025-11-09 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.
- 2025-11-09 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (consideration: CR S8036-8038; text: CR S8038)
- 2025-11-09 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2025-11-09 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S1716)
- 2025-11-09 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.
- 2025-11-09 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (consideration: CR S8036-8038; text: CR S8038)
- 2025-11-09 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2025-11-09 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/124",
    "number": "124",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A resolution recognizing the 250th anniversary of the United States Marine Corps.",
    "type": "SRES",
    "updateDate": "2026-03-12T15:09:46Z",
    "updateDateIncludingText": "2026-03-12T15:09:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (consideration: CR S8036-8038; text: CR S8038)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-11-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S1716)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-11-09",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3936 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-11-09",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3936 proposed by Senator Blumenthal. (consideration: CR S8038) To include the liberation of Helmand Province in the list of historic battles where United States Marines served.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-11-09",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-11-09",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 3936 proposed by Senator Blumenthal.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-11-09",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-11-09",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 3936 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "124",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution recognizing the 250th anniversary of the United States Marine Corps.",
          "type": "SRES",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-11-09",
          "links": {
            "link": {
              "name": "SA 3936",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/3936"
            }
          },
          "text": "Amendment SA 3936 agreed to in Senate by Unanimous Consent."
        },
        "number": "3936",
        "onBehalfOfSponsor": {
          "item": {
            "bioguideId": "B001277",
            "firstName": "Richard",
            "fullName": "Sen. Blumenthal, Richard [D-CT]",
            "lastName": "Blumenthal",
            "party": "D",
            "state": "CT",
            "type": "Proposed on behalf of"
          }
        },
        "proposedDate": "2025-11-09T05:00:00Z",
        "purpose": "To include the liberation of Helmand Province in the list of historic battles where United States Marines served.",
        "sponsors": {
          "item": {
            "bioguideId": "B001277",
            "firstName": "Richard",
            "fullName": "Sen. Blumenthal, Richard [D-CT]",
            "lastName": "Blumenthal",
            "party": "D",
            "state": "CT"
          }
        },
        "submittedDate": "2025-11-09T05:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-12T15:09:46Z"
      }
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
            "date": "2025-11-09T20:56:40Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-12T17:00:04Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "AK"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "AZ"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres124is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 124\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Blumenthal (for himself, Mr. Sullivan , Mr. Gallego , and Mr. Young ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nRecognizing the 250th anniversary of the United States Marine Corps.\nThat the Senate\u2014\n**(1)**\nrecognizes the 250th anniversary of the United States Marine Corps;\n**(2)**\nremembers and venerates the Marines and Navy corpsmen who gave their last full measure of devotion on the battlefield;\n**(3)**\naffirms the motto Semper Fidelis, embodying the honorable commitment of every Marine, past and present, who remain Always Faithful;\n**(4)**\nhonors the service and sacrifice of the men and women who serve the United States today carrying on the proud tradition of the Marines who came before them;\n**(5)**\nreaffirms the bonds of friendship and shared values between the United States Marine Corps and allied fighting forces;\n**(6)**\nsalutes the 250th year since the founding of the United States Marine Corps;\n**(7)**\ninvites the people of the United States to join in the celebration of the 250th anniversary of the United States Marine Corps by attending commemorative events, sharing stories of United States Marine Corps valor and achievement, and recognizing those who have earned the title of United States Marine over the past 250 years; and\n**(8)**\nencourages communities across the United States to recognize and honor the contributions of local Marines, and to partner with the United States Marine Corps to promote civic engagement and mutual support.",
      "versionDate": "2025-03-12",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres124ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 124\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Blumenthal (for himself, Mr. Sullivan , Mr. Gallego , and Mr. Young ) submitted the following resolution; which was referred to the Committee on Armed Services\nNovember 9, 2025 Committee discharged; considered and agreed to with an amended preamble\nRESOLUTION\nRecognizing the 250th anniversary of the United States Marine Corps.\nThat the Senate\u2014\n**(1)**\nrecognizes the 250th anniversary of the United States Marine Corps;\n**(2)**\nremembers and venerates the Marines and Navy corpsmen who gave their last full measure of devotion on the battlefield;\n**(3)**\naffirms the motto Semper Fidelis, embodying the honorable commitment of every Marine, past and present, who remain Always Faithful;\n**(4)**\nhonors the service and sacrifice of the men and women who serve the United States today carrying on the proud tradition of the Marines who came before them;\n**(5)**\nreaffirms the bonds of friendship and shared values between the United States Marine Corps and allied fighting forces;\n**(6)**\nsalutes the 250th year since the founding of the United States Marine Corps;\n**(7)**\ninvites the people of the United States to join in the celebration of the 250th anniversary of the United States Marine Corps by attending commemorative events, sharing stories of United States Marine Corps valor and achievement, and recognizing those who have earned the title of United States Marine over the past 250 years; and\n**(8)**\nencourages communities across the United States to recognize and honor the contributions of local Marines, and to partner with the United States Marine Corps to promote civic engagement and mutual support.",
      "versionDate": "2025-11-09",
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "254",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the 250th anniversary of the United States Marine Corps.",
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-14T16:03:41Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-11-14T16:04:03Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-11-14T16:03:49Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-11-14T16:03:59Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-11-14T16:03:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-09T17:00:49Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres124is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-11-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres124ats.xml"
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
      "title": "A resolution recognizing the 250th anniversary of the United States Marine Corps.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:33Z"
    },
    {
      "title": "A resolution recognizing the 250th anniversary of the United States Marine Corps.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T10:56:34Z"
    }
  ]
}
```
