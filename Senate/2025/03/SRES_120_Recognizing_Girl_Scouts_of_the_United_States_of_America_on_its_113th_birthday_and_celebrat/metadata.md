# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/120?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/120
- Title: A resolution recognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder, Juliette Gordon Low, and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.
- Congress: 119
- Bill type: SRES
- Bill number: 120
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2026-04-08T01:12:56Z
- Update date including text: 2026-04-08T01:12:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-03-26 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-03-26 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1864; text: 03/10/2025 CR S1632)
- 2025-03-26 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-03-26 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-03-26 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-03-26 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1864; text: 03/10/2025 CR S1632)
- 2025-03-26 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-03-26 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/120",
    "number": "120",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution recognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder, Juliette Gordon Low, and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.",
    "type": "SRES",
    "updateDate": "2026-04-08T01:12:56Z",
    "updateDateIncludingText": "2026-04-08T01:12:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1864; text: 03/10/2025 CR S1632)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-10",
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

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2025-03-27T01:12:08Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-10T21:15:16Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NH"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NH"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NV"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-10",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres120is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 120\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Ms. Duckworth (for herself, Ms. Collins , Mrs. Shaheen , Mr. Barrasso , Ms. Hassan , Ms. Cortez Masto , Mrs. Capito , and Mr. King ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder, Juliette Gordon Low, and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.\nThat the Senate\u2014\n**(1)**\nrecognizes Girl Scouts of the United States of America for 113 years of building girls of courage, confidence, and character, who make the world a better place;\n**(2)**\ncongratulates all Girl Scouts who earned the Gold Award in 2024;\n**(3)**\ncommemorates the trailblazing founder of Girl Scouts of the United States of America, Juliette Gordon Low, for making her mark on the currency of the United States; and\n**(4)**\nencourages Girl Scouts of the United States of America to continue to champion the ambitions, nurture the creativity, and support the talents of future women leaders.",
      "versionDate": "2025-03-10",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres120ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 120\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Ms. Duckworth (for herself, Ms. Collins , Mrs. Shaheen , Mr. Barrasso , Ms. Hassan , Ms. Cortez Masto , Mrs. Capito , and Mr. King ) submitted the following resolution; which was referred to the Committee on the Judiciary\nMarch 26, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder, Juliette Gordon Low, and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.\nThat the Senate\u2014\n**(1)**\nrecognizes Girl Scouts of the United States of America for 113 years of building girls of courage, confidence, and character, who make the world a better place;\n**(2)**\ncongratulates all Girl Scouts who earned the Gold Award in 2024;\n**(3)**\ncommemorates the trailblazing founder of Girl Scouts of the United States of America, Juliette Gordon Low, for making her mark on the currency of the United States; and\n**(4)**\nencourages Girl Scouts of the United States of America to continue to champion the ambitions, nurture the creativity, and support the talents of future women leaders.",
      "versionDate": "2025-03-10",
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
        "actionDate": "2026-03-12",
        "text": "Referred to the Committee on the Judiciary. (text: CR S1050-1051)"
      },
      "number": "641",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution recognizing Girl Scouts of the United States of America on its 114th birthday and celebrating its legacy of providing girls with a supportive and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-12",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1114",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing Girl Scouts of the United States of America on its 114th birthday and celebrating its legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "217",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder Juliette Gordon Low and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.",
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
            "updateDate": "2025-05-16T16:28:02Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-05-16T16:28:07Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-05-16T16:28:19Z"
          },
          {
            "name": "Women's education",
            "updateDate": "2025-05-16T16:28:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-14T15:00:03Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres120is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres120ats.xml"
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
      "title": "A resolution recognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder, Juliette Gordon Low, and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:34Z"
    },
    {
      "title": "A resolution recognizing Girl Scouts of the United States of America on its 113th birthday and celebrating its founder, Juliette Gordon Low, and the legacy of providing girls with a secure and inclusive space where they can explore their world, build meaningful relationships, and have access to experiences that prepare them for a life of leadership.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T10:56:19Z"
    }
  ]
}
```
