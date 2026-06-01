# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4123?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4123
- Title: End Special Treatment for Congress at Airports Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4123
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-20T15:25:17Z
- Update date including text: 2026-04-20T15:25:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-03-19 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S1355-1356)
- 2026-03-19 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S1356)
- 2026-03-19 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-03-19 - Discharge: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- 2026-03-19 - Committee: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 14:02:35 - Floor: Received in the House.
- 2026-03-24 14:11:54 - Floor: Held at the desk.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-03-19 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S1355-1356)
- 2026-03-19 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S1356)
- 2026-03-19 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-03-19 - Discharge: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- 2026-03-19 - Committee: Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 14:02:35 - Floor: Received in the House.
- 2026-03-24 14:11:54 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4123",
    "number": "4123",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "End Special Treatment for Congress at Airports Act of 2026",
    "type": "S",
    "updateDate": "2026-04-20T15:25:17Z",
    "updateDateIncludingText": "2026-04-20T15:25:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-03-24",
      "actionTime": "14:11:54",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-03-24",
      "actionTime": "14:02:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (text: CR S1356)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S1355-1356)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Commerce, Science, and Transportation discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-17",
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
                "actionDate": "2026-03-19",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4707 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2026-03-19",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 4707 proposed by Senator Cornyn. (consideration: CR S1355-1356) To amend the definition of Trusted Traveler Program.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-03-19",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2026-03-19",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 4707 proposed by Senator Cornyn.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-03-19",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2026-03-19",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 4707 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "4123",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "End Special Treatment for Congress at Airports Act of 2026",
          "type": "S",
          "updateDateIncludingText": "2026-04-20"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2026-03-19",
          "links": {
            "link": {
              "name": "SA 4707",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/4707"
            }
          },
          "text": "Amendment SA 4707 agreed to in Senate by Unanimous Consent."
        },
        "number": "4707",
        "onBehalfOfSponsor": {
          "item": {
            "bioguideId": "C001056",
            "firstName": "John",
            "fullName": "Sen. Cornyn, John [R-TX]",
            "lastName": "Cornyn",
            "party": "R",
            "state": "TX",
            "type": "Proposed on behalf of"
          }
        },
        "proposedDate": "2026-03-19T04:00:00Z",
        "purpose": "To amend the definition of Trusted Traveler Program.",
        "sponsors": {
          "item": {
            "bioguideId": "C001056",
            "firstName": "John",
            "fullName": "Sen. Cornyn, John [R-TX]",
            "lastName": "Cornyn",
            "party": "R",
            "state": "TX"
          }
        },
        "submittedDate": "2026-03-19T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-23T16:20:58Z"
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
            "date": "2026-03-20T00:46:49Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-17T23:34:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4123is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4123\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Cornyn introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit preferential screening for Members of Congress at airports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Special Treatment for Congress at Airports Act of 2026 .\n#### 2. Definitions\nIn this Act\u2014\n**(1) Administrator**\nThe term Administrator means the Administrator of the Transportation Security Administration.\n**(2) Member of Congress**\nThe term Member of Congress has the meaning given that term in section 13101 of title 5, United States Code.\n**(3) Screening location**\nThe term screening location has the meaning given that term in section 1540.5 of title 49, Code of Federal Regulations.\n**(4) Trusted Traveler Program**\nThe term Trusted Traveler Program means a voluntary program of the Department that allows U.S. Customs and Border Protection to expedite clearance of pre-approved, low-risk travelers arriving in the United States.\n#### 3. Requirement for standard security screening\n##### (a) In general\nNone of the funds appropriated or otherwise made available to the Transportation Security Administration shall be used to provide or facilitate the provision of a Member of Congress with expedited or preferential access to or through security screenings required pursuant to section 44901 of title 49, United States Code.\n##### (b) No expedited access\nA Member of Congress may not\u2014\n**(1)**\nbypass standard screening procedures of the Transportation Security Administration; or\n**(2)**\nreceive priority or expedited access to a screening location on the basis of the official position of such Member of Congress.\n#### 4. Rule of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto limit the authority of the Transportation Security Administration to implement risk-based security programs available to the general public; or\n**(2)**\nto prohibit Members of Congress from participating in a publicly available Trusted Traveler Program, provided such participation is not based on the official positions of such Members of Congress.\n#### 5. Enforcement\n##### (a) Policy Implementation\nThe Administrator shall update policies and procedures as necessary to ensure compliance with this Act.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Administrator shall submit to Congress a report on the implementation of, and compliance with, this Act.",
      "versionDate": "2026-03-17",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4123es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 4123\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo prohibit preferential screening for Members of Congress at airports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Special Treatment for Congress at Airports Act of 2026 .\n#### 2. Definitions\nIn this Act\u2014\n**(1) Administrator**\nThe term Administrator means the Administrator of the Transportation Security Administration.\n**(2) Member of Congress**\nThe term Member of Congress has the meaning given that term in section 13101 of title 5, United States Code.\n**(3) Screening location**\nThe term screening location has the meaning given that term in section 1540.5 of title 49, Code of Federal Regulations.\n**(4) Trusted Traveler Program**\nThe term Trusted Traveler Program means any of the following:\n**(A)**\nGlobal Entry.\n**(B)**\nThe PreCheck Program.\n**(C)**\nSENTRI.\n**(D)**\nNEXUS.\n**(E)**\nAny other United States Government program that issues a unique identifier, such as a known traveler number, that the Transportation Security Administration accepts as validating that the individual holding such identifier is a member of a known low-risk population.\n**(F)**\nAny other program implemented by the Transportation Security Administration under section 109(a)(3) of the Aviation and Transportation Security Act ( 49 U.S.C. 114 note; Public Law 107\u201371 ).\n#### 3. Requirement for standard security screening\n##### (a) In general\nNone of the funds appropriated or otherwise made available to the Transportation Security Administration shall be used to provide or facilitate the provision of a Member of Congress with expedited or preferential access to or through security screenings required pursuant to section 44901 of title 49, United States Code.\n##### (b) No expedited access\nA Member of Congress shall not\u2014\n**(1)**\nbe exempt from Federal passenger and baggage screening procedures of the Transportation Security Administration; or\n**(2)**\nreceive priority or expedited access to a screening location on the basis of the official position of such Member of Congress.\n#### 4. Rule of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto limit the authority of the Transportation Security Administration to implement risk-based security programs available to the general public; or\n**(2)**\nto prohibit Members of Congress from participating in a publicly available Trusted Traveler Program, provided such participation is not based on the official positions of such Members of Congress.\n#### 5. Enforcement\n##### (a) Policy Implementation\nThe Administrator shall update policies and procedures as necessary to ensure compliance with this Act.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Administrator shall submit to Congress a report on the implementation of, and compliance with, this Act.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2026-03-24",
        "text": "Referred to the House Committee on Homeland Security."
      },
      "number": "8049",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "End Special Treatment for Congress at Airports Act of 2026",
      "type": "HR"
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
            "name": "Aviation and airports",
            "updateDate": "2026-03-23T15:07:57Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-03-23T15:07:52Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2026-03-23T15:15:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-20T14:21:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-19",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s4123",
          "measure-number": "4123",
          "measure-type": "s",
          "orig-publish-date": "2026-03-19",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4123v55",
            "update-date": "2026-04-20"
          },
          "action-date": "2026-03-19",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>End Special Treatment for Congress at Airports Act of 2026</strong></p><p>This bill prohibits the Transportation Security Administration (TSA) from providing a Member of Congress with expedited or preferential access to or through airport security screenings.</p><p>Specifically, TSA funds may not be used to\u00a0</p><ul><li>exempt a Member of Congress from\u00a0TSA passenger and baggage screening, or</li><li>provide a Member of Congress with priority or expedited access to a screening location based on their position.</li></ul><p>TSA must update its policies and procedures to ensure compliance with this\u00a0bill.</p>"
        },
        "title": "End Special Treatment for Congress at Airports Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4123.xml",
    "summary": {
      "actionDate": "2026-03-19",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>End Special Treatment for Congress at Airports Act of 2026</strong></p><p>This bill prohibits the Transportation Security Administration (TSA) from providing a Member of Congress with expedited or preferential access to or through airport security screenings.</p><p>Specifically, TSA funds may not be used to\u00a0</p><ul><li>exempt a Member of Congress from\u00a0TSA passenger and baggage screening, or</li><li>provide a Member of Congress with priority or expedited access to a screening location based on their position.</li></ul><p>TSA must update its policies and procedures to ensure compliance with this\u00a0bill.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s4123"
    },
    "title": "End Special Treatment for Congress at Airports Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-19",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>End Special Treatment for Congress at Airports Act of 2026</strong></p><p>This bill prohibits the Transportation Security Administration (TSA) from providing a Member of Congress with expedited or preferential access to or through airport security screenings.</p><p>Specifically, TSA funds may not be used to\u00a0</p><ul><li>exempt a Member of Congress from\u00a0TSA passenger and baggage screening, or</li><li>provide a Member of Congress with priority or expedited access to a screening location based on their position.</li></ul><p>TSA must update its policies and procedures to ensure compliance with this\u00a0bill.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s4123"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4123is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4123es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "End Special Treatment for Congress at Airports Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "End Special Treatment for Congress at Airports Act of 2026",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-20T04:53:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Special Treatment for Congress at Airports Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T13:23:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit preferential screening for Members of Congress at airports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T13:18:19Z"
    }
  ]
}
```
