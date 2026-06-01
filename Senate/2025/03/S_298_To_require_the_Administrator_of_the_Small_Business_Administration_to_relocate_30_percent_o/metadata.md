# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/298?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/298
- Title: Returning SBA to Main Street Act
- Congress: 119
- Bill type: S
- Bill number: 298
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-11-18T08:15:35Z
- Update date including text: 2025-11-18T08:15:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-20 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 21.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-20 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 21.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/298",
    "number": "298",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Returning SBA to Main Street Act",
    "type": "S",
    "updateDate": "2025-11-18T08:15:35Z",
    "updateDateIncludingText": "2025-11-18T08:15:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 21.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2025-03-04T22:08:23Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-21T00:57:33Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T17:49:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s298is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 298\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Ernst (for herself, Mrs. Blackburn , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo require the Administrator of the Small Business Administration to relocate 30 percent of the employees assigned to headquarters to duty stations outside the Washington metropolitan area, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Returning SBA to Main Street Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administration; Administrator**\nThe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively.\n**(2) Budget justification materials**\nThe term budget justification materials has the meaning given that term in section 3(b)(2)(A) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).\n**(3) Employee**\nThe term employee has the meaning given that term in section 2105 of title 5, United States Code.\n**(4) Headquarters employee of the Administration**\nThe term headquarters employee of the Administration means\u2014\n**(A)**\nan employee of the Administration whose permanent duty station is at the headquarters of the Administration; or\n**(B)**\nan employee of the Administration\u2014\n**(i)**\nwho teleworks on a full-time basis; and\n**(ii)**\nwhose rate of pay is calculated based on the Washington metropolitan area rate of pay.\n**(5) Headquarters of the Administration**\nThe term headquarters of the Administration means the building serving as the principal managerial and administrative center of the Administration, in accordance with section 4(a) of the Small Business Act ( 15 U.S.C. 633(a) ).\n**(6) Pay locality**\nThe term pay locality has the meaning given that term in section 5302 of title 5, United States Code.\n**(7) Rural**\nThe term rural means any area that is not designated as an urban area, based on the most recent data available from the Bureau of the Census.\n**(8) Telework**\nThe term telework has the meaning given that term in section 6501 of title 5, United States Code.\n**(9) Telework on a full-time basis**\nThe term telework on a full-time basis means that an employee is authorized to telework for 100 percent of the work days of the employee per pay period.\n**(10) Washington metropolitan area**\nThe term Washington metropolitan area means the geographic area to which the Washington metropolitan area rate of pay applies.\n**(11) Washington metropolitan area rate of pay**\nThe term Washington metropolitan area rate of pay means the rate of pay in effect for the pay locality designated as Washington-Baltimore-Arlington, DC-MD-VA-WV-PA .\n#### 3. Relocation of employees\n##### (a) In general\nNotwithstanding any other provisions of law, and not later than 1 year after the date of enactment of this Act, the Administrator shall\u2014\n**(1)**\nchange the permanent duty station of not less than 30 percent of the headquarters employees of the Administration, as of the date of enactment of this Act, to be at an office of the Administration at a location outside the Washington metropolitan area, which shall be at locations throughout the regions of the Administration; and\n**(2)**\nfor each employee of the Administration whose permanent duty station is changed under paragraph (1), ensure that\u2014\n**(A)**\nthe rate of pay of the employee is calculated based on the pay locality for the permanent duty station of the employee; and\n**(B)**\nthe employee is not authorized to telework on a full-time basis.\n##### (b) Determination of new duty stations\nIn determining the permanent duty stations of headquarters employees of the Administration under subsection (a), the Administrator shall\u2014\n**(1)**\npromote geographic diversity, including consideration of rural markets; and\n**(2)**\nensure adequate staffing throughout the regions of the Administration, to promote in-person customer service.\n##### (c) Determination of employees eligible for a change in duty station\n**(1) In general**\nExcept as provided in paragraph (2), the Administrator shall include each headquarters employee of the Administration as eligible for a change in permanent duty station under subsection (a).\n**(2) Exception**\nA headquarters employee of the Administration who is a qualified individual who receives an accommodation to telework on a full-time basis as a reasonable accommodation under title I of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12111 et seq. )\u2014\n**(A)**\nshall not be determined to be eligible for a change in permanent duty station under subsection (a); and\n**(B)**\nshall be counted as a headquarters employee of the Administration for purposes of complying with subsection (a)(1).\n**(3) Notice of determination of eligibility**\nNot later than the day before the date on which the Administrator submits the report required under subsection (d), the Administrator shall notify each headquarters employee of the Administration who the Administrator determines is eligible for a change in permanent duty station under subsection (a) of that determination.\n##### (d) Report\nNot later than 180 days after the date of enactment of this Act, the Administrator shall submit to the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives a report that provides\u2014\n**(1)**\nthe number of headquarters employees of the Administration, as of the date of enactment of this Act;\n**(2)**\nthe number of headquarters employees of the Administration identified as eligible for a change in permanent duty station, in accordance with subsection (c);\n**(3)**\nthe number of headquarters employees of the Administration whose permanent duty station will be changed to be at an office of the Administration at a location outside the Washington metropolitan area under subsection (a);\n**(4)**\nthe number of headquarters employees of the Administration subject to an exception under subsection (c)(2); and\n**(5)**\nthe plan of the Administrator to implement subsection (a).\n##### (e) Implementation\n**(1) In general**\nNot earlier than 60 days, and not later than 90 days, after the date on which the Administrator submits the report required under subsection (d), the Administrator shall notify each headquarters employee of the Administration whose permanent duty station will be changed to be at an office of the Administration located outside the Washington metropolitan area under subsection (a)\u2014\n**(A)**\nthat, effective 90 days after the date of the notification\u2014\n**(i)**\nthe permanent duty station of the employee shall be changed;\n**(ii)**\nthe rate of pay of the employee shall be calculated based on the pay locality for such permanent duty station; and\n**(iii)**\nthe employee shall not be authorized to telework on a full-time basis; and\n**(B)**\nof the location of such permanent duty station.\n**(2) Full-time teleworkers remaining in the Washington metropolitan area**\n**(A) In general**\nFor any employee described in subparagraph (B), effective on the date that is 180 days after the date on which the Administrator submits the report required under subsection (d), the employee shall not be authorized to telework on a full-time basis.\n**(B) Employees covered**\nAn employee described in this subparagraph is a headquarters employee of the Administration\u2014\n**(i)**\nwho teleworks on a full-time basis, as of the date of enactment of this Act;\n**(ii)**\nwho is not subject to an exception under subsection (c)(2); and\n**(iii)**\nwhose permanent duty station is not changed to be an office of the Administration at a location outside the Washington metropolitan area under subsection (a).\n**(3) No relocation incentives**\nIf, pursuant to this Act, the official worksite (as defined in section 531.605 of title 5, Code of Federal Regulations, or any successor regulation) of an employee changes from the residence of the employee to the headquarters of the Administration, notwithstanding any other provision of law, the employee shall not be paid any relocation incentive.\n#### 4. Reduction in headquarters office space\n##### (a) In general\nThe Administrator shall reduce the amount of office space for the headquarters of the Administration by not less than 30 percent.\n##### (b) Implementation\nThe Administrator shall\u2014\n**(1)**\nbegin reducing office space under subsection (a) not later than 180 days after the date of enactment of this Act; and\n**(2)**\ncomplete the reduction of office space required under subsection (a) not later than 2 years after the date of enactment of this Act.\n#### 5. Information included in budget justification materials provided to Congress\nThe Administrator shall include in the first budget justification materials of the Administration submitted after the date of enactment of this Act, and the budget justification materials of the Administration for each fiscal year thereafter\u2014\n**(1)**\nthe number of headquarters employees of the Administration;\n**(2)**\nthe number of employees of the Administration assigned to a permanent duty station in\u2014\n**(A)**\na field office of the Administration;\n**(B)**\na district office of the Administration; or\n**(C)**\na regional office of the Administration;\n**(3)**\nthe number of employees of the Administration who telework on a full-time basis; and\n**(4)**\nthe number of employees of the Administration who are a qualified individual who receives an accommodation to telework on a full-time basis as a reasonable accommodation under title I of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12111 et seq. ).\n#### 6. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act and the application of the provision to any other person or circumstance shall not be affected thereby.\n#### 7. Supersession\nThis Act shall supersede any other provision of law and any provision of a collective bargaining agreement or master labor agreement.\n#### 8. No private cause of action\nNothing in this Act shall be construed to establish a private cause of action, equitable or otherwise, to challenge any selection, change, or decision made, or action taken, under this Act.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s298rs.xml",
      "text": "II\nCalendar No. 21\n119th CONGRESS\n1st Session\nS. 298\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Ernst (for herself, Mrs. Blackburn , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nMarch 4, 2025 Reported by Ms. Ernst , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Administrator of the Small Business Administration to relocate 30 percent of the employees assigned to headquarters to duty stations outside the Washington metropolitan area, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Returning SBA to Main Street Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administration; Administrator**\nThe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively.\n**(2) Budget justification materials**\nThe term budget justification materials has the meaning given that term in section 3(b)(2)(A) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).\n**(3) Employee**\nThe term employee has the meaning given that term in section 2105 of title 5, United States Code.\n**(4) Headquarters employee of the Administration**\nThe term headquarters employee of the Administration means\u2014\n**(A)**\nan employee of the Administration whose permanent duty station is at the headquarters of the Administration; or\n**(B)**\nan employee of the Administration\u2014\n**(i)**\nwho teleworks on a full-time basis; and\n**(ii)**\nwhose rate of pay is calculated based on the Washington metropolitan area rate of pay.\n**(5) Headquarters of the Administration**\nThe term headquarters of the Administration means the building serving as the principal managerial and administrative center of the Administration, in accordance with section 4(a) of the Small Business Act ( 15 U.S.C. 633(a) ).\n**(6) Pay locality**\nThe term pay locality has the meaning given that term in section 5302 of title 5, United States Code.\n**(7) Rural**\nThe term rural means any area that is not designated as an urban area, based on the most recent data available from the Bureau of the Census.\n**(8) Telework**\nThe term telework has the meaning given that term in section 6501 of title 5, United States Code.\n**(9) Telework on a full-time basis**\nThe term telework on a full-time basis means that an employee is authorized to telework for 100 percent of the work days of the employee per pay period.\n**(10) Washington metropolitan area**\nThe term Washington metropolitan area means the geographic area to which the Washington metropolitan area rate of pay applies.\n**(11) Washington metropolitan area rate of pay**\nThe term Washington metropolitan area rate of pay means the rate of pay in effect for the pay locality designated as Washington-Baltimore-Arlington, DC-MD-VA-WV-PA .\n#### 3. Relocation of employees\n##### (a) In general\nNotwithstanding any other provisions of law, and not later than 1 year after the date of enactment of this Act, the Administrator shall\u2014\n**(1)**\nchange the permanent duty station of not less than 30 percent of the headquarters employees of the Administration, as of the date of enactment of this Act, to be at an office of the Administration at a location outside the Washington metropolitan area, which shall be at locations throughout the regions of the Administration; and\n**(2)**\nfor each employee of the Administration whose permanent duty station is changed under paragraph (1), ensure that\u2014\n**(A)**\nthe rate of pay of the employee is calculated based on the pay locality for the permanent duty station of the employee; and\n**(B)**\nthe employee is not authorized to telework on a full-time basis.\n##### (b) Determination of new duty stations\nIn determining the permanent duty stations of headquarters employees of the Administration under subsection (a), the Administrator shall\u2014\n**(1)**\npromote geographic diversity, including consideration of rural markets; and\n**(2)**\nensure adequate staffing throughout the regions of the Administration, to promote in-person customer service.\n##### (c) Determination of employees eligible for a change in duty station\n**(1) In general**\nExcept as provided in paragraph (2), the Administrator shall include each headquarters employee of the Administration as eligible for a change in permanent duty station under subsection (a).\n**(2) Exception**\nA headquarters employee of the Administration who is a qualified individual who receives an accommodation to telework on a full-time basis as a reasonable accommodation under title I of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12111 et seq. )\u2014\n**(A)**\nshall not be determined to be eligible for a change in permanent duty station under subsection (a); and\n**(B)**\nshall be counted as a headquarters employee of the Administration for purposes of complying with subsection (a)(1).\n**(3) Notice of determination of eligibility**\nNot later than the day before the date on which the Administrator submits the report required under subsection (d), the Administrator shall notify each headquarters employee of the Administration who the Administrator determines is eligible for a change in permanent duty station under subsection (a) of that determination.\n##### (d) Report\nNot later than 180 days after the date of enactment of this Act, the Administrator shall submit to the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives a report that provides\u2014\n**(1)**\nthe number of headquarters employees of the Administration, as of the date of enactment of this Act;\n**(2)**\nthe number of headquarters employees of the Administration identified as eligible for a change in permanent duty station, in accordance with subsection (c);\n**(3)**\nthe number of headquarters employees of the Administration whose permanent duty station will be changed to be at an office of the Administration at a location outside the Washington metropolitan area under subsection (a);\n**(4)**\nthe number of headquarters employees of the Administration subject to an exception under subsection (c)(2); and\n**(5)**\nthe plan of the Administrator to implement subsection (a).\n##### (e) Implementation\n**(1) In general**\nNot earlier than 60 days, and not later than 90 days, after the date on which the Administrator submits the report required under subsection (d), the Administrator shall notify each headquarters employee of the Administration whose permanent duty station will be changed to be at an office of the Administration located outside the Washington metropolitan area under subsection (a)\u2014\n**(A)**\nthat, effective 90 days after the date of the notification\u2014\n**(i)**\nthe permanent duty station of the employee shall be changed;\n**(ii)**\nthe rate of pay of the employee shall be calculated based on the pay locality for such permanent duty station; and\n**(iii)**\nthe employee shall not be authorized to telework on a full-time basis; and\n**(B)**\nof the location of such permanent duty station.\n**(2) Full-time teleworkers remaining in the Washington metropolitan area**\n**(A) In general**\nFor any employee described in subparagraph (B), effective on the date that is 180 days after the date on which the Administrator submits the report required under subsection (d), the employee shall not be authorized to telework on a full-time basis.\n**(B) Employees covered**\nAn employee described in this subparagraph is a headquarters employee of the Administration\u2014\n**(i)**\nwho teleworks on a full-time basis, as of the date of enactment of this Act;\n**(ii)**\nwho is not subject to an exception under subsection (c)(2); and\n**(iii)**\nwhose permanent duty station is not changed to be an office of the Administration at a location outside the Washington metropolitan area under subsection (a).\n**(3) No relocation incentives**\nIf, pursuant to this Act, the official worksite (as defined in section 531.605 of title 5, Code of Federal Regulations, or any successor regulation) of an employee changes from the residence of the employee to the headquarters of the Administration, notwithstanding any other provision of law, the employee shall not be paid any relocation incentive.\n#### 4. Reduction in headquarters office space\n##### (a) In general\nThe Administrator shall reduce the amount of office space for the headquarters of the Administration by not less than 30 percent.\n##### (b) Implementation\nThe Administrator shall\u2014\n**(1)**\nbegin reducing office space under subsection (a) not later than 180 days after the date of enactment of this Act; and\n**(2)**\ncomplete the reduction of office space required under subsection (a) not later than 2 years after the date of enactment of this Act.\n#### 5. Information included in budget justification materials provided to Congress\nThe Administrator shall include in the first budget justification materials of the Administration submitted after the date of enactment of this Act, and the budget justification materials of the Administration for each fiscal year thereafter\u2014\n**(1)**\nthe number of headquarters employees of the Administration;\n**(2)**\nthe number of employees of the Administration assigned to a permanent duty station in\u2014\n**(A)**\na field office of the Administration;\n**(B)**\na district office of the Administration; or\n**(C)**\na regional office of the Administration;\n**(3)**\nthe number of employees of the Administration who telework on a full-time basis; and\n**(4)**\nthe number of employees of the Administration who are a qualified individual who receives an accommodation to telework on a full-time basis as a reasonable accommodation under title I of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12111 et seq. ).\n#### 6. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act and the application of the provision to any other person or circumstance shall not be affected thereby.\n#### 7. Supersession\nThis Act shall supersede any other provision of law and any provision of a collective bargaining agreement or master labor agreement.\n#### 8. No private cause of action\nNothing in this Act shall be construed to establish a private cause of action, equitable or otherwise, to challenge any selection, change, or decision made, or action taken, under this Act.",
      "versionDate": "2025-03-04",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-05-21",
        "text": "Placed on the Union Calendar, Calendar No. 80."
      },
      "number": "2027",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Returning SBA to Main Street Act of 2025",
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
            "name": "Administrative remedies",
            "updateDate": "2025-03-19T13:42:52Z"
          },
          {
            "name": "Commuting",
            "updateDate": "2025-03-19T13:46:47Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-19T13:15:39Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-03-19T13:18:53Z"
          },
          {
            "name": "Small Business Administration",
            "updateDate": "2025-03-19T13:15:14Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-03-19T13:19:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-03T12:23:09Z"
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
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s298is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s298rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Returning SBA to Main Street Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "title": "Returning SBA to Main Street Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Returning SBA to Main Street Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T14:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Small Business Administration to relocate 30 percent of the employees assigned to headquarters to duty stations outside the Washington metropolitan area, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T14:18:26Z"
    }
  ]
}
```
