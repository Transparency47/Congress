# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/178
- Title: Ensuring Accurate and Complete Abortion Data Reporting Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 178
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-12-06T06:47:20Z
- Update date including text: 2025-12-06T06:47:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/178",
    "number": "178",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Ensuring Accurate and Complete Abortion Data Reporting Act of 2025",
    "type": "S",
    "updateDate": "2025-12-06T06:47:20Z",
    "updateDateIncludingText": "2025-12-06T06:47:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
        "item": {
          "date": "2025-01-22T16:22:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "OK"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ND"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "NE"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ID"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s178is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 178\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Ms. Ernst (for herself, Mr. Lankford , Mr. Daines , Mr. Cramer , Mrs. Fischer , Mr. Hagerty , Mr. Risch , Mr. Hawley , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act and the Public Health Service Act to improve the reporting of abortion data to the Centers for Disease Control and Prevention, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Accurate and Complete Abortion Data Reporting Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nReporting abortion data has been voluntary in the past, which has not resulted in complete data being submitted to the Centers for Disease Control and Prevention.\n**(2)**\nWhile the Centers for Disease Control and Prevention requests specific data points from each State and the District of Columbia, there is a great variety in the information collected and published by the States.\n**(3)**\nIn fact, there is not a single abortion data point publicly reported for all 50 States and the District of Columbia.\n**(4)**\nEven more alarming, 3 States that together account for 15 percent of the United States population of women of childbearing age do not report any abortion data to the Centers for Disease Control and Prevention.\n**(5)**\nAccurate statistical data regarding abortion and those who survive abortion attempts is critical to public health and policy analysis.\n#### 3. Medicaid payments for certain family planning services and supplies contingent on submission of abortion data to CDC\nSection 1903 of the Social Security Act ( 42 U.S.C. 1396b ) is amended\u2014\n**(1)**\nin subsection (a)(5), by inserting before an amount equal to the following: subject to subsection (cc), ; and\n**(2)**\nby adding at the end the following new subsection:\n(cc) Annual reports on abortion data (1) In general Subject to paragraph (2), as a condition of receiving payment under subsection (a)(5) with respect to any amount expended during a year (beginning with the year following 2 years after the date of the enactment of this subsection) for family planning services and supplies described in section 1905(a)(4)(C) furnished to an individual described in section 1902(ii) or an individual whose medical assistance under this title is limited to such services and supplies furnished pursuant to a waiver granted under section 1115, each State shall, by not later than December 31 of the previous year, submit to the abortion surveillance system of the Centers for Disease Control and Prevention, with respect to the year before the previous year, at least abortion data regarding the mandatory questions described in section 317W(a)(3)(A) of the Public Health Service Act. (2) Late submission of reports With respect to a year, in the case of a State that does not submit by December 31 of the previous year the abortion data required under paragraph (1) with respect to the year before the previous year but submits such data by December 31 of the year, such State shall continue to receive payment, including retroactive payment, under subsection (a)(5) with respect to any amount expended during the year for family planning services and supplies described in section 1905(a)(4)(C) furnished to an individual described in such paragraph. (3) Certification of abortion data (A) In general With respect to each submission of abortion data under this subsection, a State shall certify to the Director of the Centers for Disease Control and Prevention that such data is accurate. (B) False information In the case that the Director of the Centers for Disease Control and Prevention determines that a State has knowingly provided false information with respect to a submission of abortion data under this subsection, such State may not receive payment under subsection (a)(5) with respect to any amount expended during the first full fiscal year following such determination for family planning services and supplies described in section 1905(a)(4)(C) furnished to an individual described in paragraph (1). .\n#### 4. Collection of abortion data by CDC\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by inserting after section 317V the following:\n317W. Abortion data (a) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall\u2014 (1) maintain a surveillance system to collect aggregate data in a standardized format on abortions in the United States; (2) as part of such system, create a standard worksheet to collect data from States on abortions in the respective States, which\u2014 (A) shall, at a minimum, include questions on the variables listed in subsection (b), to be treated as mandatory questions for purposes of section 1903(cc) of the Social Security Act; and (B) may include such additional questions on abortion as the Secretary determines to be appropriate, to be treated as voluntary questions; (3) as part of such system, allow for cross-tabulation of the variables listed in subsection (b), including cross-tabulation of maternal age by gestational age; race and ethnicity by gestational age; type of abortion procedure by gestational age; race and ethnicity by maternal age; and race and ethnicity by marital status; and (4) periodically update the questions in the worksheet under paragraph (2), including the classification of such questions as mandatory or voluntary. (b) Variables The variables listed in this subsection are the following: (1) Maternal age in years. (2) Gestational age in completed weeks at the time of abortion. (3) Maternal race. (4) Maternal ethnicity. (5) Maternal race by ethnicity. (6) The abortion method type. (7) Maternal marital status. (8) Previous pregnancies of the mother, including the number of previous live births, the number of previous induced abortions, and the number of previous spontaneous abortions. (9) Maternal residence (limited to county and State). (10) Whether the child survived the abortion. (c) Technical assistance The Secretary shall provide technical assistance to States to facilitate and improve the reporting of data to the system under subsection (a). (d) Annual reporting The Secretary shall\u2014 (1) issue an annual report on abortion, which shall include the data collected pursuant to this section; and (2) publish such report not later than December 30 of the third calendar year following the calendar year covered by the report. .",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "627",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Accurate and Complete Abortion Data Reporting Act of 2025",
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
            "name": "Abortion",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Child health",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Family planning and birth control",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-17T14:12:08Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-03-17T14:12:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T13:57:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119s178",
          "measure-number": "178",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s178v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ensuring Accurate and Complete Abortion Data Reporting Act of 2025</strong><strong></strong></p><p>This bill requires states, as a condition of federal payment under Medicaid for family planning services, to report certain abortion data to the Centers for Disease Control and Prevention (CDC). (Currently, reporting is voluntary.) The CDC must develop standardized questions for states with respect to specified variables (e.g., maternal demographics and methods of abortion).</p>"
        },
        "title": "Ensuring Accurate and Complete Abortion Data Reporting Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s178.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Accurate and Complete Abortion Data Reporting Act of 2025</strong><strong></strong></p><p>This bill requires states, as a condition of federal payment under Medicaid for family planning services, to report certain abortion data to the Centers for Disease Control and Prevention (CDC). (Currently, reporting is voluntary.) The CDC must develop standardized questions for states with respect to specified variables (e.g., maternal demographics and methods of abortion).</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s178"
    },
    "title": "Ensuring Accurate and Complete Abortion Data Reporting Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Accurate and Complete Abortion Data Reporting Act of 2025</strong><strong></strong></p><p>This bill requires states, as a condition of federal payment under Medicaid for family planning services, to report certain abortion data to the Centers for Disease Control and Prevention (CDC). (Currently, reporting is voluntary.) The CDC must develop standardized questions for states with respect to specified variables (e.g., maternal demographics and methods of abortion).</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s178"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s178is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Ensuring Accurate and Complete Abortion Data Reporting Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-04T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Accurate and Complete Abortion Data Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act and the Public Health Service Act to improve the reporting of abortion data to the Centers for Disease Control and Prevention, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:33:32Z"
    }
  ]
}
```
