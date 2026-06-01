# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1866
- Title: SCREENS for Cancer Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1866
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-02-11T12:03:24Z
- Update date including text: 2026-02-11T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1866",
    "number": "1866",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "SCREENS for Cancer Act of 2025",
    "type": "S",
    "updateDate": "2026-02-11T12:03:24Z",
    "updateDateIncludingText": "2026-02-11T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
            "date": "2025-05-22T16:24:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T16:24:49Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "ME"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AR"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "SD"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1866is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1866\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Ms. Baldwin (for herself, Ms. Collins , Ms. Cortez Masto , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize and improve the National Breast and Cervical Cancer Early Detection Program for fiscal years 2026 through 2030, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Screening for Communities to Receive Early and Equitable Needed Services for Cancer Act of 2025 or the SCREENS for Cancer Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2025, there will be more than 319,750 new cases of invasive breast cancer and nearly 43,000 breast cancer deaths in the United States.\n**(2)**\nIn 2025, there will be about 13,360 new cases of invasive cervical cancer and about 4,320 deaths from cervical cancer.\n**(3)**\nSince its creation in 1991, the National Breast and Cervical Cancer Early Detection Program (referred to in this section as the NBCCEDP ) has provided lifesaving cancer screening and diagnostic services to low-income, uninsured, or underinsured women in all 50 States, the District of Columbia, 6 territories, and 13 Tribes or Tribal organizations.\n**(4)**\nNBCCEDP places special emphasis on outreach to women who are geographically or culturally isolated.\n**(5)**\nNBCCEDP has served more than 6,400,000 people and provided more than 16,500,000 breast and cervical cancer screening examinations.\n**(6)**\nThese screening exams have diagnosed nearly 80,000 invasive breast cancers and more than 25,000 premalignant breast lesions, as well as almost 5,300 invasive cervical cancers and over 248,000 premalignant cervical lesions, of which 38 percent were high-grade.\n**(7)**\nThe program also provides public education, outreach, patient navigation, and care coordination to increase breast and cervical cancer screening rates.\n**(8)**\nReauthorizing NBCCEDP will result in expanded services, leading to more people being screened and more cancers diagnosed at earlier stages.\n#### 3. National Breast and Cervical Cancer Early Detection Program\nTitle XV of the Public Health Service Act ( 42 U.S.C. 300k et seq. ) is amended\u2014\n**(1)**\nin section 1501 ( 42 U.S.C. 300k )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (2), by striking the provision of appropriate follow-up services and support services such as case management and inserting that appropriate follow-up services are provided ;\n**(ii)**\nin paragraph (3), by striking programs for the detection and control and inserting for the prevention, detection, and control ;\n**(iii)**\nin paragraph (4), by striking the detection and control and inserting the prevention, detection, and control ;\n**(iv)**\nin paragraph (5)\u2014\n**(I)**\nby striking monitor and inserting ensure ; and\n**(II)**\nby striking ; and and inserting a semicolon;\n**(v)**\nby redesignating paragraph (6) as paragraph (9);\n**(vi)**\nby inserting after paragraph (5) the following:\n(6) to enhance appropriate support activities to increase breast and cervical cancer screening, such as navigation of health care services, implementation of evidence-based or evidence-informed strategies proven to increase breast and cervical cancer screening in health care settings, and facilitation of access to health care settings that provide breast and cervical cancer screenings; (7) to reduce disparities in incidents of and deaths due to breast and cervical cancer in populations with higher-than-average rates; (8) to improve equitable access to breast and cervical cancer screening and diagnostic services and to reduce related barriers, including due to factors that relate to negative health outcomes; and ; and\n**(vii)**\nin paragraph (9), as so redesignated, by striking through (5) and inserting through (8) ; and\n**(B)**\nby striking subsection (d);\n**(2)**\nin section 1503 ( 42 U.S.C. 300m )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking that, initially and all that follows through the semicolon and inserting that appropriate breast and cervical cancer screening and diagnostic services are provided consistent with relevant evidence-based recommendations; and ;\n**(ii)**\nby striking paragraphs (2) and (4);\n**(iii)**\nby redesignating paragraph (3) as paragraph (2); and\n**(iv)**\nin paragraph (2), as so redesignated, by striking ; and and inserting a period; and\n**(B)**\nby striking subsection (d);\n**(3)**\nin section 1508(b) ( 42 U.S.C. 300n\u20134(b) )\u2014\n**(A)**\nby striking 1 year after the date of the enactment of the National Breast and Cervical Cancer Early Detection Program Reauthorization of 2007, and annually thereafter, and inserting 2 years after the date of enactment of the Screening for Communities to Receive Early and Equitable Needed Services for Cancer Act of 2025 , and every 5 years thereafter, ;\n**(B)**\nby striking Labor and Human Resources and inserting Health, Education, Labor, and Pensions ; and\n**(C)**\nby striking preceding fiscal year and inserting preceding 2 fiscal years in the case of the first report after the date of enactment of the Screening for Communities to Receive Early and Equitable Needed Services for Cancer Act of 2025 and preceding 5 fiscal years for each report thereafter ; and\n**(4)**\nin section 1510(a) ( 42 U.S.C. 300n\u20135(a) )\u2014\n**(A)**\nby striking and after 2011, ; and\n**(B)**\nby inserting , and $235,000,000 for each of fiscal years 2026 through 2030 before the period at the end.\n#### 4. GAO study\nNot later than September 30, 2027, the Comptroller General of the United States shall report to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives on the work of the National Breast and Cervical Cancer Early Detection Program, including\u2014\n**(1)**\nan estimate of the number of individuals eligible for services provided under such program;\n**(2)**\na summary of trends in the number of individuals served through such program; and\n**(3)**\nan assessment of any factors that may be driving the trends identified under paragraph (2), including any barriers to accessing breast and cervical cancer screenings provided by such program.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2381",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SCREENS for Cancer Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-13T13:43:50Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1866is.xml"
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
      "title": "SCREENS for Cancer Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SCREENS for Cancer Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Screening for Communities to Receive Early and Equitable Needed Services for Cancer Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize and improve the National Breast and Cervical Cancer Early Detection Program for fiscal years 2026 through 2030, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:23Z"
    }
  ]
}
```
