# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/371?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/371
- Title: A resolution honoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.
- Congress: 119
- Bill type: SRES
- Bill number: 371
- Origin chamber: Senate
- Introduced date: 2025-09-02
- Update date: 2026-03-12T15:08:57Z
- Update date including text: 2026-03-12T15:08:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in Senate
- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S5566-5567)
- 2025-09-08 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S6439)
- 2025-09-08 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S6439: 2)
- 2025-09-08 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S6439)
- 2025-09-08 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-09-08 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-09-02: Introduced in Senate

## Actions

- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S5566-5567)
- 2025-09-08 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S6439)
- 2025-09-08 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S6439: 2)
- 2025-09-08 - Floor: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S6439)
- 2025-09-08 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-09-08 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/371",
    "number": "371",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution honoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.",
    "type": "SRES",
    "updateDate": "2026-03-12T15:08:57Z",
    "updateDateIncludingText": "2026-03-12T15:08:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S6439)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and an amended preamble by Unanimous Consent. (text: CR S6439: 2)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S6439)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S5566-5567)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-02",
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
                "actionDate": "2025-09-08",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3827 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-09-08",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3827 proposed by Senator Moran for Senator Klobuchar. (consideration: CR S6439) To correct a capitalization error.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-09-08",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-09-08",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 3827 proposed by Senator Moran for Senator Klobuchar.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-09-08",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-09-08",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 3827 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "371",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A resolution honoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.",
          "type": "SRES",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-09-08",
          "links": {
            "link": {
              "name": "SA 3827",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/3827"
            }
          },
          "text": "Amendment SA 3827 agreed to in Senate by Unanimous Consent."
        },
        "number": "3827",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "M000934",
              "firstName": "Jerry",
              "fullName": "Sen. Moran, Jerry [R-KS]",
              "lastName": "Moran",
              "party": "R",
              "state": "KS",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "M000934",
              "firstName": "Jerry",
              "fullName": "Sen. Moran, Jerry [R-KS]",
              "lastName": "Moran",
              "party": "R",
              "state": "KS",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2025-09-08T04:00:00Z",
        "purpose": "To correct a capitalization error.",
        "sponsors": {
          "item": {
            "bioguideId": "K000367",
            "firstName": "Amy",
            "fullName": "Sen. Klobuchar, Amy [D-MN]",
            "lastName": "Klobuchar",
            "party": "D",
            "state": "MN"
          }
        },
        "submittedDate": "2025-09-08T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-12T15:08:57Z"
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
            "date": "2025-09-08T22:59:39Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-09-02T22:37:53Z",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres371is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 371\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Ms. Klobuchar (for herself and Ms. Smith ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.\nThat the Senate\u2014\n**(1)**\ncondemns this senseless act of violence and offers its condolences to the families and loved ones of those killed and injured in the tragedy;\n**(2)**\nhonors the memory of the victims and stands in solidarity with survivors, the Catholic community, and the broader Minneapolis community;\n**(3)**\ncommends the bravery and service of law enforcement, first responders, school and church staff, and community members who acted swiftly to protect and help others;\n**(4)**\nstands with the Annunciation Catholic Church and School community and all Minnesotans in the face of this terrible tragedy;\n**(5)**\nexpresses hope that the Annunciation community, together with other communities scarred by gun violence across the country, will heal through unity, compassion, and shared faith;\n**(6)**\ndeclares that there is no place for violence in our communities, and that everyone deserves to feel safe in their sacred places of worship and schools; and\n**(7)**\nexpresses solidarity with all faith communities and schools that have been scarred by such violence.",
      "versionDate": "2025-09-02",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres371ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 371\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Ms. Klobuchar (for herself and Ms. Smith ) submitted the following resolution; which was referred to the Committee on the Judiciary\nSeptember 8, 2025 Committee discharged; considered and agreed to with an amended preamble\nRESOLUTION\nHonoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.\nThat the Senate\u2014\n**(1)**\ncondemns this senseless act of violence and offers its condolences to the families and loved ones of those killed and injured in the tragedy;\n**(2)**\nhonors the memory of the victims and stands in solidarity with survivors, the Catholic community, and the broader Minneapolis community;\n**(3)**\ncommends the bravery and service of law enforcement, first responders, school and church staff, and community members who acted swiftly to protect and help others;\n**(4)**\nstands with the Annunciation Catholic Church and School community and all Minnesotans in the face of this terrible tragedy;\n**(5)**\nexpresses hope that the Annunciation community, together with other communities scarred by gun violence across the country, will heal through unity, compassion, and shared faith;\n**(6)**\ndeclares that there is no place for violence in our communities, and that everyone deserves to feel safe in their sacred places of worship and schools; and\n**(7)**\nexpresses solidarity with all faith communities and schools that have been scarred by such violence.",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-09-02",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "669",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Honoring the victims and survivors of the mass shooting at Annunciation Catholic Church and School in Minneapolis, Minnesota.",
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
            "name": "Congressional tributes",
            "updateDate": "2025-09-23T15:00:32Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-09-23T15:01:32Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-09-23T15:01:40Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-09-23T15:01:50Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2025-09-23T15:01:27Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-09-23T15:01:36Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-09-23T15:01:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-22T12:08:10Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres371is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres371ats.xml"
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
      "title": "A resolution honoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-04T02:03:20Z"
    },
    {
      "title": "A resolution honoring the victims and survivors of the mass shooting at the Annunciation Catholic Church and School in Minneapolis, Minnesota.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T10:56:20Z"
    }
  ]
}
```
