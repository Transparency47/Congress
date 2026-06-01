# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1276
- Title: American Innovation Act
- Congress: 119
- Bill type: S
- Bill number: 1276
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2025-12-05T21:59:22Z
- Update date including text: 2025-12-05T21:59:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2174-2175)
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2174-2175)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1276",
    "number": "1276",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "American Innovation Act",
    "type": "S",
    "updateDate": "2025-12-05T21:59:22Z",
    "updateDateIncludingText": "2025-12-05T21:59:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2174-2175)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:50:32Z",
          "name": "Referred To"
        }
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1276is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1276\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Durbin (for himself, Ms. Duckworth , Ms. Hirono , Mr. Padilla , and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prioritize funding for an expanded and sustained national investment in basic science research.\n#### 1. Short title\nThis Act may be cited as the American Innovation Act .\n#### 2. Appropriations for innovation\n##### (a) In general\nThere are hereby authorized to be appropriated, and appropriated, out of any monies in the Treasury not otherwise appropriated, the following:\n**(1) National science foundation**\nFor the National Science Foundation\u2014\n**(A)**\nfor fiscal year 2026, $9,735,000,000;\n**(B)**\nfor fiscal year 2027, $10,447,000,000;\n**(C)**\nfor fiscal year 2028, $11,205,000,000;\n**(D)**\nfor fiscal year 2029, $12,016,000,000;\n**(E)**\nfor fiscal year 2030, $12,886,000,000;\n**(F)**\nfor fiscal year 2031, $13,818,000,000;\n**(G)**\nfor fiscal year 2032, $14,818,000,000;\n**(H)**\nfor fiscal year 2033, $15,892,000,000;\n**(I)**\nfor fiscal year 2034, $17,043,000,000;\n**(J)**\nfor fiscal year 2035, $18,279,000,000; and\n**(K)**\nfor fiscal year 2036 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(2) Department of energy, office of science**\nFor the Office of Science at the Department of Energy\u2014\n**(A)**\nfor fiscal year 2026, $8,854,000,000;\n**(B)**\nfor fiscal year 2027, $9,501,000,000;\n**(C)**\nfor fiscal year 2028, $10,191,000,000;\n**(D)**\nfor fiscal year 2029, $10,929,000,000;\n**(E)**\nfor fiscal year 2030, $11,720,000,000;\n**(F)**\nfor fiscal year 2031, $12,568,000,000;\n**(G)**\nfor fiscal year 2032, $13,477,000,000;\n**(H)**\nfor fiscal year 2033, $14,453,000,000;\n**(I)**\nfor fiscal year 2034, $15,501,000,000;\n**(J)**\nfor fiscal year 2035, $16,624,000,000; and\n**(K)**\nfor fiscal year 2036 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(3) Department of defense science and technology programs**\nFor the Department of Defense science and technology programs\u2014\n**(A)**\nfor fiscal year 2026, $23,109,000,000;\n**(B)**\nfor fiscal year 2027, $24,799,000,000;\n**(C)**\nfor fiscal year 2028, $26,259,000,000;\n**(D)**\nfor fiscal year 2029, $28,525,000,000;\n**(E)**\nfor fiscal year 2030, $30,590,000,000;\n**(F)**\nfor fiscal year 2031, $32,803,000,000;\n**(G)**\nfor fiscal year 2032, $35,178,000,000;\n**(H)**\nfor fiscal year 2033, $37,725,000,000;\n**(I)**\nfor fiscal year 2034, $40,459,000,000;\n**(J)**\nfor fiscal year 2035, $43,392,000,000; and\n**(K)**\nfor fiscal year 2036 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(4) National institute of standards and technology scientific and technical research and services**\nFor the scientific and technical research and services of the National Institute of Standards and Technology at the Department of Commerce\u2014\n**(A)**\nfor fiscal year 2026, $1,244,000,000;\n**(B)**\nfor fiscal year 2027, $1,335,000,000;\n**(C)**\nfor fiscal year 2028, $1,431,000,000;\n**(D)**\nfor fiscal year 2029, $1,535,000,000;\n**(E)**\nfor fiscal year 2030, $1,646,000,000;\n**(F)**\nfor fiscal year 2031, $1,765,000,000;\n**(G)**\nfor fiscal year 2032, $1,893,000,000;\n**(H)**\nfor fiscal year 2033, $2,030,000,000;\n**(I)**\nfor fiscal year 2034, $2,177,000,000;\n**(J)**\nfor fiscal year 2035, $2,335,000,000; and\n**(K)**\nfor fiscal year 2036 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n**(5) National aeronautics and space administration science mission directorate**\nFor the Science Mission Directorate at the National Aeronautics and Space Administration\u2014\n**(A)**\nfor fiscal year 2026, $7,880,000,000;\n**(B)**\nfor fiscal year 2027, $8,457,000,000;\n**(C)**\nfor fiscal year 2028, $9,070,000,000;\n**(D)**\nfor fiscal year 2029, $9,727,000,000;\n**(E)**\nfor fiscal year 2030, $10,431,000,000;\n**(F)**\nfor fiscal year 2031, $11,186,000,000;\n**(G)**\nfor fiscal year 2032, $11,995,000,000;\n**(H)**\nfor fiscal year 2033, $12,864,000,000;\n**(I)**\nfor fiscal year 2034, $13,796,000,000;\n**(J)**\nfor fiscal year 2035, $14,796,000,000; and\n**(K)**\nfor fiscal year 2036 and each fiscal year thereafter, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase (if any), during the previous fiscal year, in the Consumer Price Index for all urban consumers published by the Bureau of Labor Statistics.\n##### (b) Availability\nAmounts appropriated under subsection (a) shall remain available until expended.\n##### (c) Definitions\nIn this section:\n**(1) Department of defense science and technology programs**\nThe term Department of Defense science and technology programs means the appropriations accounts that support the various institutes, offices, and centers that make up the Department of Defense science and technology programs.\n**(2) National science foundation**\nThe term National Science Foundation means the appropriations accounts that support the various institutes, offices, and centers that make up the National Science Foundation.\n**(3) Office of science at the department of energy**\nThe term Office of Science at the Department of Energy means the appropriations accounts that support the various institutes, offices, and centers that make up the Department of Energy Office of Science.\n**(4) Science mission directorate at the national aeronautics and space administration**\nThe term Science Mission Directorate at the National Aeronautics and Space Administration means the appropriations accounts that support the various institutes, offices, and centers that make up the National Aeronautics and Space Administration Science Mission Directorate.\n**(5) Scientific and technical research and services of the national institute of standards and technology**\nThe term scientific and technical research and services of the National Institute of Standards and Technology means the appropriations accounts that support the various institutes, offices, and centers that make up the National Institute of Standards and Technology scientific and technical research and services.\n##### (d) Exemption of certain appropriations from sequestration\n**(1) In general**\nSection 255(g)(1)(A) of the Balanced Budget and Emergency Deficit Control Act ( 2 U.S.C. 905(g)(1)(A) ) is amended by inserting after Advances to the Unemployment Trust Fund and Other Funds (16\u20130327\u20130\u20131\u2013600). the following:\nAppropriations under the American Innovation Act. .\n**(2) Applicability**\nThe amendment made by this section shall apply to any sequestration order issued under the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900 et seq. ) on or after the date of enactment of this Act.\n##### (e) Budgetary effects\n**(1) Statutory paygo scorecards**\nThe budgetary effects of this section shall not be entered on either PAYGO scorecard maintained pursuant to section 4(d) of the Statutory Pay As-You-Go Act of 2010 ( 2 U.S.C. 933(d) ).\n**(2) Senate paygo scorecards**\nThe budgetary effects of this section shall not be entered on any PAYGO scorecard maintained for purposes of section 4106 of H. Con. Res. 71 (115th Congress).",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-04-03",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Armed Services, and the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2628",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Innovation Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-01T17:41:59Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1276is.xml"
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
      "title": "American Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prioritize funding for an expanded and sustained national investment in basic science research.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:51Z"
    }
  ]
}
```
