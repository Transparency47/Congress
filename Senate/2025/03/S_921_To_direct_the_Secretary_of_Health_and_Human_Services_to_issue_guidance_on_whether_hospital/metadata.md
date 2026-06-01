# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/921?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/921
- Title: Tyler’s Law
- Congress: 119
- Bill type: S
- Bill number: 921
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2026-04-08T18:35:54Z
- Update date including text: 2026-04-08T18:35:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-01-15 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 307.
- 2026-03-23 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S1559-1560; text: CR S1559-1560)
- 2026-03-23 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 14:02:32 - Floor: Received in the House.
- 2026-03-24 14:11:36 - Floor: Held at the desk.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-01-15 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 307.
- 2026-03-23 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S1559-1560; text: CR S1559-1560)
- 2026-03-23 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 14:02:32 - Floor: Received in the House.
- 2026-03-24 14:11:36 - Floor: Held at the desk.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/921",
    "number": "921",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Tyler\u2019s Law",
    "type": "S",
    "updateDate": "2026-04-08T18:35:54Z",
    "updateDateIncludingText": "2026-04-08T18:35:54Z"
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
      "actionTime": "14:11:36",
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
      "actionTime": "14:02:32",
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
      "actionDate": "2026-03-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S1559-1560; text: CR S1559-1560)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 307.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-01-28",
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
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
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
            "date": "2026-01-28T19:54:31Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-15T15:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-10T22:37:41Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-10T22:37:41Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "VA"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "FL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "OK"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NH"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "AL"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s921is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 921\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mr. Banks (for himself, Mr. Padilla , Mr. Grassley , Mr. Warner , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services to issue guidance on whether hospital emergency departments should implement fentanyl testing as a routine procedure for patients experiencing an overdose, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Tyler\u2019s Law .\n#### 2. Testing for fentanyl in hospital emergency departments\n##### (a) Study\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall complete a study to determine\u2014\n**(1)**\nhow frequently hospital emergency departments test for fentanyl (in addition to testing for other substances such as amphetamines, phencyclidine, cocaine, opiates, and marijuana) when a patient is experiencing an overdose;\n**(2)**\nthe costs associated with such testing for fentanyl;\n**(3)**\nthe potential benefits and risks for patients receiving such testing for fentanyl; and\n**(4)**\nhow fentanyl testing in hospital emergency departments may impact the experience of the patient, including\u2014\n**(A)**\nprotections for the confidentiality and privacy of the patient\u2019s personal health information; and\n**(B)**\nthe patient-physician relationship.\n##### (b) Guidance\nNot later than 6 months after completion of the study under subsection (a), based on the results of such study, the Secretary of Health and Human Services shall issue guidance on the following:\n**(1)**\nWhether hospital emergency departments should implement fentanyl testing as a routine procedure for patients experiencing an overdose.\n**(2)**\nHow hospitals can ensure that clinicians in their hospital emergency departments are aware of which substances are being tested for in their routinely-administered drug tests, regardless of whether those tests screen for fentanyl.\n**(3)**\nHow the administration of fentanyl testing in hospital emergency departments may affect the future risk of overdose and general health outcomes.\n##### (c) Definition\nIn this section, the term hospital emergency department means a hospital emergency department as such term is used in section 1867(a) of the Social Security Act ( 42 U.S.C. 1395dd(a) ).",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s921rs.xml",
      "text": "II\nCalendar No. 307\n119th CONGRESS\n2d Session\nS. 921\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mr. Banks (for himself, Mr. Padilla , Mr. Grassley , Mr. Warner , Mr. Young , Mr. Scott of Florida , Mr. Mullin , Mr. Kim , Ms. Klobuchar , Mr. Warnock , Ms. Hassan , Mrs. Moody , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nJanuary 28, 2026 Reported by Mr. Cassidy , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo direct the Secretary of Health and Human Services to issue guidance on whether hospital emergency departments should implement fentanyl testing as a routine procedure for patients experiencing an overdose, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Tyler\u2019s Law .\n#### 2. Testing for fentanyl in hospital emergency departments\n##### (a) Study\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall complete a study to determine\u2014\n**(1)**\nhow frequently hospital emergency departments test for fentanyl (in addition to testing for other substances such as amphetamines, phencyclidine, cocaine, opiates, and marijuana) when a patient is experiencing an overdose;\n**(2)**\nthe costs associated with such testing for fentanyl;\n**(3)**\nthe potential benefits and risks for patients receiving such testing for fentanyl; and\n**(4)**\nhow fentanyl testing in hospital emergency departments may impact the experience of the patient, including\u2014\n**(A)**\nprotections for the confidentiality and privacy of the patient\u2019s personal health information; and\n**(B)**\nthe patient-physician relationship.\n##### (b) Guidance\nNot later than 6 months after completion of the study under subsection (a), based on the results of such study, the Secretary of Health and Human Services shall issue guidance on the following:\n**(1)**\nWhether hospital emergency departments should implement fentanyl testing as a routine procedure for patients experiencing an overdose.\n**(2)**\nHow hospitals can ensure that clinicians in their hospital emergency departments are aware of which substances are being tested for in their routinely-administered drug tests, regardless of whether those tests screen for fentanyl.\n**(3)**\nHow the administration of fentanyl testing in hospital emergency departments may affect the future risk of overdose and general health outcomes.\n##### (c) Definition\nIn this section, the term hospital emergency department means a hospital emergency department as such term is used in section 1867(a) of the Social Security Act ( 42 U.S.C. 1395dd(a) ).",
      "versionDate": "2026-01-28",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s921es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 921\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo direct the Secretary of Health and Human Services to issue guidance on whether hospital emergency departments should implement fentanyl testing as a routine procedure for patients experiencing an overdose, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Tyler\u2019s Law .\n#### 2. Testing for fentanyl in hospital emergency departments\n##### (a) Study\nNot later than 3 years after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use and in coordination with other Federal departments, agencies, or stakeholders, as appropriate, shall complete a study to determine\u2014\n**(1)**\nhow frequently hospital emergency departments test for fentanyl or fentanyl-related substances when a patient is experiencing an overdose, and test for other controlled substances related to such an overdose;\n**(2)**\nscenarios in which hospital emergency departments do not administer tests for fentanyl or fentanyl-related substances when a patient is experiencing an overdose, or for other controlled substances related to such an overdose;\n**(3)**\nthe costs associated with such testing for fentanyl or fentanyl-related substances;\n**(4)**\nthe potential benefits and risks for patients receiving such testing for fentanyl or fentanyl-related substances;\n**(5)**\npotential staff training needs to support testing for fentanyl or fentanyl-related substances;\n**(6)**\nhow testing for fentanyl or fentanyl-related substances in hospital emergency departments may impact the experience of the patient, including\u2014\n**(A)**\nprotections for the privacy and security of the patient\u2019s protected health information (as defined in section 160.103 of title 45, Code of Federal Regulations (or any successor regulations)) under part 160 of title 45, Code of Federal Regulations, and subparts C and E of part 164 of title 45, Code of Federal Regulations (or any successor regulations); and\n**(B)**\nthe patient-health care professional relationship; and\n**(7)**\nbarriers that hospital emergency departments may encounter when trying to implement testing for fentanyl or fentanyl-related substances and recommendations on how best to address those barriers.\n##### (b) Guidance\nNot later than 9 months after completion of the study under subsection (a), based on the results of such study, the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use and in coordination with other Federal departments, agencies, or stakeholders, as appropriate, shall issue guidance on the following:\n**(1)**\nWhether hospital emergency departments should implement testing for fentanyl or fentanyl-related substances as a routine procedure for patients experiencing an overdose.\n**(2)**\nHow hospitals can ensure that health care professionals in their hospital emergency departments are aware of which substances are being tested for in their routinely-administered drug tests, regardless of whether those tests screen for fentanyl or fentanyl-related substances.\n**(3)**\nHow the administration of testing for fentanyl or fentanyl-related substances in hospital emergency departments may affect the future risk of overdose and health outcomes.\n**(4)**\nAvailable Federal resources that can assist hospital emergency departments in implementing testing for fentanyl or fentanyl-related substances.\n##### (c) Definitions\nIn this section, the term hospital emergency department means an emergency department of a hospital or an independent freestanding emergency department (as such terms are defined in section 2799A\u20131(a)(3) of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111(a)(3) )).",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2026-03-10T18:37:24Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2026-03-10T18:37:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-10T18:37:24Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-10T18:37:24Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2026-03-10T18:37:24Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2026-03-10T18:37:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-03-26T15:52:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s921is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s921rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s921es.xml"
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
      "title": "Tyler\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Tyler\u2019s Law",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-24T05:08:19Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Tyler\u2019s Law",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-01-30T04:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tyler\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services to issue guidance on whether hospital emergency departments should implement fentanyl testing as a routine procedure for patients experiencing an overdose, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:48Z"
    }
  ]
}
```
