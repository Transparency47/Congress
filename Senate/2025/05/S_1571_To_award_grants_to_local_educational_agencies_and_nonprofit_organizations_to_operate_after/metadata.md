# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1571
- Title: AFTER SCHOOL Act
- Congress: 119
- Bill type: S
- Bill number: 1571
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1571",
    "number": "1571",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "AFTER SCHOOL Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T17:10:13Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1571is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1571\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mrs. Blackburn (for herself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo award grants to local educational agencies and nonprofit organizations to operate after school programs in certain areas with a high rate of juvenile crime.\n#### 1. Short title\nThis Act may be cited as the Advancing Frequent and Tailored Education to Rebuild Safe Communities and Help Orchestrate Opportunities and Learning Act or the AFTER SCHOOL Act .\n#### 2. Grants for after school programs\n##### (a) Definitions\nIn this section:\n**(1) ESEA terms**\nThe terms local educational agency and secondary school have the meanings given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Eligible applicant**\nThe term eligible applicant means an eligible local educational agency or an eligible nonprofit organization.\n**(3) Eligible local educational agency**\nThe term eligible local educational agency means a local educational agency that serves 1 or more secondary schools that are located in a county in which the juvenile offense rate for the most recent fiscal year for which data is available was not less than 10 percent.\n**(4) Eligible nonprofit organization**\nThe term eligible nonprofit organization means an organization described in section 501(c)(3) and exempt from tax under section 501(a) of the Internal Revenue Code of 1986 that\u2014\n**(A)**\nhas experience in operating an after school program or similar program for secondary school students; and\n**(B)**\nis located in a county in which the juvenile offense rate for the most recent fiscal year for which data is available was not less than 10 percent.\n**(5) Eligible students**\nThe term eligible students means students in any of grades 6 through 12.\n**(6) Juvenile offense rate**\nThe term juvenile offense rate means the percentage of violent offenses committed by any individual who is not more than 19 years of age as compared to the total number of violent offenses committed by all age groups in a given county, as published in the Uniform Crime Reporting Program of the Federal Bureau of Investigation.\n##### (b) Program established\nThe Attorney General shall award grants, in accordance with subsection (c), to eligible applicants that have an approved application in order to enable those eligible applicants to provide after school programs for eligible students, as described in subsection (f).\n##### (c) Formula\nFrom the total amount made available to carry out this section, the Attorney General shall allot to each eligible applicant having an application approved under subsection (e), an amount that bears the same relationship to that total amount as the number of eligible students who will be served by such eligible applicant under this section bears to the number of eligible students who will be served by all eligible applicants under this section.\n##### (d) Notice of eligibility\nOn the first day of the first fiscal year beginning after the date of enactment of this Act, and of each fiscal year thereafter, the Attorney General shall\u2014\n**(1)**\ndetermine which counties in the United States had a juvenile offense rate of not less than 10 percent during the most recent fiscal year for which data is available;\n**(2)**\npublish the determination of the Attorney General under paragraph (1); and\n**(3)**\npublish an application that eligible applicants seeking a grant under this section can submit.\n##### (e) Application\nAn eligible applicant seeking a grant under this section shall submit the application described in subsection (d)(3) to the Attorney General at such time, in such manner, and containing such information as the Attorney General may require, including\u2014\n**(1)**\nthe juvenile offense rate for the most recent fiscal year for which data are available for\u2014\n**(A)**\nif the eligible applicant is an eligible local educational agency, the county in which 1 or more secondary schools served by the eligible local educational agency are located; or\n**(B)**\nif the eligible applicant is an eligible nonprofit organization, the county in which the eligible nonprofit organization is located;\n**(2)**\nan assurance that the eligible applicant\u2014\n**(A)**\nif the eligible applicant is an eligible local educational agency, will carry out the after school programs or will partner only with an eligible nonprofit organization to carry out such programs; or\n**(B)**\nif the eligible applicant is an eligible nonprofit organization, will carry out the after school programs; and\n**(3)**\ninformation about the activities and frequency of the after school programs that will be carried out with grant funds under this section.\n##### (f) Uses of funds\n**(1) In general**\nAn eligible applicant that receives a grant under this section shall use such grant funds to operate after school programs for eligible students, which may include\u2014\n**(A)**\nexpanding existing after school programs for eligible students;\n**(B)**\ndeveloping and carrying out new after school programs for eligible students; or\n**(C)**\nif the eligible applicant is an eligible local educational agency, partnering with an eligible nonprofit organization to administer and operate after school programs for eligible students.\n**(2) Comprehensive program activities**\nAn eligible applicant that receives a grant under this section shall ensure that the after school programs carried out with grant funds are programs that\u2014\n**(A)**\nare held when school is out of session; and\n**(B)**\ninclude activities that have an educational purpose that aim to\u2014\n**(i)**\nexpand learning opportunities,\n**(ii)**\nfoster foundational skill development,\n**(iii)**\nprovide youth leadership opportunities; and\n**(iv)**\nprovide a safe and supportive environment.\n##### (g) Reports\n**(1) Eligible applicant reports**\nEach eligible applicant that receives a grant under this section shall submit an annual report to the Attorney General that describes\u2014\n**(A)**\nthe number of schools served by an after school program established or maintained using funds under this section;\n**(B)**\nthe number of children served at each such school; and\n**(C)**\nthe general successes and vulnerabilities of the after school programs established or maintained using funds under this section.\n**(2) Attorney General report**\nNot later than 90 days after the date as of which the Attorney General has received all the reports for a year under paragraph (1), the Attorney General shall submit to Congress a report summarizing the reports received under that paragraph.\n##### (h) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $15,000,000 for each of fiscal years 2026, 2027, 2028, and 2029, to remain available until expended.",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in Senate"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-21T12:42:24Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1571is.xml"
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
      "title": "AFTER SCHOOL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AFTER SCHOOL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Frequent and Tailored Education to Rebuild Safe Communities and Help Orchestrate Opportunities and Learning Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to award grants to local educational agencies and nonprofit organizations to operate after school programs in certain areas with a high rate of juvenile crime.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:26Z"
    }
  ]
}
```
