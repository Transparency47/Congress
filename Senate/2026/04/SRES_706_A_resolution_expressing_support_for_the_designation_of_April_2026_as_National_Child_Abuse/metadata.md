# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/706?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/706
- Title: A resolution expressing support for the designation of April 2026 as "National Child Abuse Prevention Month", and the goals and ideals of National Child Abuse Prevention Month.
- Congress: 119
- Bill type: SRES
- Bill number: 706
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-18T20:51:37Z
- Update date including text: 2026-05-19T00:48:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2136-2137)
- 2026-04-29 - IntroReferral: Submitted in Senate
- 2026-05-14 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-14 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2313)
- 2026-05-14 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2026-05-14 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- Latest action: 2026-04-29: Submitted in Senate

## Actions

- 2026-04-29 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2136-2137)
- 2026-04-29 - IntroReferral: Submitted in Senate
- 2026-05-14 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-14 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2313)
- 2026-05-14 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.
- 2026-05-14 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/706",
    "number": "706",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "A resolution expressing support for the designation of April 2026 as \"National Child Abuse Prevention Month\", and the goals and ideals of National Child Abuse Prevention Month.",
    "type": "SRES",
    "updateDate": "2026-05-18T20:51:37Z",
    "updateDateIncludingText": "2026-05-19T00:48:47Z"
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
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2136-2137)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
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
            "date": "2026-05-14T18:30:45Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-29T22:58:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "WV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres706is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 706\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Cornyn (for himself, Ms. Blunt Rochester , Mrs. Blackburn , Mr. Hickenlooper , Mrs. Capito , Mr. Luj\u00e1n , and Ms. Hassan ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of April 2026 as National Child Abuse Prevention Month , and the goals and ideals of National Child Abuse Prevention Month.\nThat the Senate\u2014\n**(1)**\nsupports the designation of April 2026 as National Child Abuse Prevention Month ;\n**(2)**\nexpresses support for the goals and ideals of National Child Abuse Prevention Month;\n**(3)**\nrecognizes that child abuse and neglect and child sexual abuse are preventable and that a healthy and prosperous society depends on strong families and communities;\n**(4)**\nsupports efforts to increase the awareness of, and provide education for, the general public of the United States, with respect to preventing child abuse and neglect and building protective factors for families;\n**(5)**\nsupports the efforts to help survivors of childhood sexual abuse heal;\n**(6)**\nsupports justice for victims of childhood sexual abuse; and\n**(7)**\nrecognizes the need for prevention, healing, and justice efforts related to childhood abuse, neglect, and sexual abuse.",
      "versionDate": "2026-04-29",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres706ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 706\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Cornyn (for himself, Ms. Blunt Rochester , Mrs. Blackburn , Mr. Hickenlooper , Mrs. Capito , Mr. Luj\u00e1n , and Ms. Hassan ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nMay 14, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nExpressing support for the designation of April 2026 as National Child Abuse Prevention Month , and the goals and ideals of National Child Abuse Prevention Month.\nThat the Senate\u2014\n**(1)**\nsupports the designation of April 2026 as National Child Abuse Prevention Month ;\n**(2)**\nexpresses support for the goals and ideals of National Child Abuse Prevention Month;\n**(3)**\nrecognizes that child abuse and neglect and child sexual abuse are preventable and that a healthy and prosperous society depends on strong families and communities;\n**(4)**\nsupports efforts to increase the awareness of, and provide education for, the general public of the United States, with respect to preventing child abuse and neglect and building protective factors for families;\n**(5)**\nsupports the efforts to help survivors of childhood sexual abuse heal;\n**(6)**\nsupports justice for victims of childhood sexual abuse; and\n**(7)**\nrecognizes the need for prevention, healing, and justice efforts related to childhood abuse, neglect, and sexual abuse.",
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
        "actionDate": "2025-04-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2643; text: CR S2668-2669)"
      },
      "number": "184",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of April 2025 as \"National Child Abuse Prevention Month\", and the goals and ideals of National Child Abuse Prevention Month.",
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
            "name": "Child safety and welfare",
            "updateDate": "2026-05-18T15:58:41Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2026-05-18T15:58:41Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-05-18T15:58:41Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2026-05-18T15:58:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-05-18T20:51:37Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres706is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres706ats.xml"
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
      "title": "A resolution expressing support for the designation of April 2026 as \"National Child Abuse Prevention Month\", and the goals and ideals of National Child Abuse Prevention Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:18:24Z"
    },
    {
      "title": "A resolution expressing support for the designation of April 2026 as \"National Child Abuse Prevention Month\", and the goals and ideals of National Child Abuse Prevention Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T10:56:27Z"
    }
  ]
}
```
