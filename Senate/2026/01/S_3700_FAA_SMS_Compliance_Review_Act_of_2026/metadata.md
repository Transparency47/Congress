# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3700
- Title: FAA SMS Compliance Review Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3700
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-04-07T15:45:06Z
- Update date including text: 2026-04-07T15:45:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3700",
    "number": "3700",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "FAA SMS Compliance Review Act of 2026",
    "type": "S",
    "updateDate": "2026-04-07T15:45:06Z",
    "updateDateIncludingText": "2026-04-07T15:45:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
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
            "date": "2026-02-12T15:00:10Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-27T22:12:49Z",
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
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "VA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "VT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3700is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3700\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Ms. Cantwell (for herself, Ms. Duckworth , Mr. Markey , Mr. Warner , Mrs. Shaheen , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish an expert review panel to make recommendations for a comprehensive agency-wide safety management system at the FAA.\n#### 1. Short title\nThis Act may be cited as the FAA SMS Compliance Review Act of 2026 .\n#### 2. Expert compliance review of FAA Safety Management System\n##### (a) Expert compliance review\n**(1) Establishment**\n**(A) In general**\nNot later than 60 days after the date of enactment of this section, the Administrator shall convene an independent expert panel (in this section referred to as the review panel ) to review and make findings and recommendations on the matters listed in paragraph (2).\n**(B) Purpose**\nThe purpose of the review panel is to review and evaluate FAA orders and policies to inform the FAA\u2019s implementation of a comprehensive and integrated SMS within the FAA.\n**(2) Contents of review**\nThe review panel shall review the following:\n**(A)**\nThe extent to which the FAA\u2019s SMS complies with relevant FAA orders and policies.\n**(B)**\nThe actual and projected safety enhancements achieved through the FAA\u2019s prior implementation of SMS.\n**(C)**\nThe effectiveness of SMS, including with respect to the implementation of the following 4 components:\n**(i)**\nSafety policy.\n**(ii)**\nSafety risk management.\n**(iii)**\nSafety assurance.\n**(iv)**\nSafety promotion.\n**(D)**\nThe extent to which the FAA\u2019s safety culture promotes or fosters the SMS consistent with the principles of the ICAO's Safety Management Manual (Doc. 9859) or any similar successor document.\n**(E)**\nThe effectiveness of FAA\u2019s internal audit process to determine, at minimum, the performance of FAA\u2019s SMS.\n**(F)**\nThe extent to which SMS and each of the 4 components described in subparagraph (C) are integrated appropriately among and across lines of business of the FAA.\n**(G)**\nThe extent to which SMS and each of the 4 components so described are understood by, communicated to, and included in training for, personnel at the FAA.\n**(H)**\nThe efficacy of existing SMS in place at applicable lines of business at the FAA including, but not limited to, the Air Traffic Organization, the Aviation Safety Office, and the Office of Airports.\n**(I)**\nThe efficacy of the FAA\u2019s Voluntary Safety Reporting Programs as part of SMS, including the efficacy of specific voluntary safety reporting programs at applicable lines of business, and any actions taken by the FAA in response to reports filed under such programs.\n**(J)**\nWhether the Federal Government should advocate for changes to Annex 19\u2013Safety Management of the ICAO to ensure appropriate updates to the State Safety Program standards and recommended practices, including\u2014\n**(i)**\na systems-level approach to evaluating and improving SMS for air navigation service providers; and\n**(ii)**\nthe implementation of SMS for civil aviation regulators.\n**(K)**\nAny other matter determined by the Administrator for which review by the review panel would be consistent with the public interest in aviation safety.\n**(3) Composition of review panel**\n**(A) Appointed members**\nThe review panel shall consist of the following members appointed by the Administrator:\n**(i)**\nTwo representatives of the National Aeronautics and Space Administration with expertise in SMSs.\n**(ii)**\nFive appropriately qualified representatives of aviation labor organizations (designated by the applicable represented organization), including\u2014\n**(I)**\norganizations representing certified collective bargaining representatives of airline pilots; and\n**(II)**\nthe exclusive bargaining representatives of FAA air traffic controllers certified under section 7111 of title 5, United States Code.\n**(iii)**\nNot less than 5 independent subject matter experts in safety management systems who\u2014\n**(I)**\nhave not served as a political appointee in the FAA; and\n**(II)**\nhave a minimum of 10 years of relevant applied experience.\n**(iv)**\nTwo air carrier employees whose job responsibilities include administration of a SMS.\n**(v)**\nTwo individuals representing holders of a certificate issued under part 21 of title 14, Code of Federal Regulations, whose job responsibilities include administration of a SMS.\n**(vi)**\nTwo other representatives from the aerospace industry that do not meet the criteria described in clause (iv) or (v) and who have expertise in SMS or whose job responsibilities include administration of a SMS.\n**(vii)**\nA representative of the United States Mission to the ICAO.\n**(viii)**\nA representative from the National Transportation Safety Board, as a non-voting member.\n**(B) Advisory members**\n**(i) In general**\nIn addition to the appointed members described in subparagraph (A), the review panel shall be advised by up to 5 employees of the FAA, at least 3 of whom shall be subject matter experts in implementing SMS at the FAA.\n**(ii) Duties**\nThe advisory members may take part in deliberations of the review panel and provide subject matter expertise with respect to the review panel\u2019s work.\n**(4) Recommendations**\nThe review panel shall issue recommendations to the Administrator based on the review of the matters listed in paragraph (2) in order to inform the FAA\u2019s implementation of a comprehensive and integrated SMS for lines of business within the FAA.\n**(5) Report**\n**(A) Submission**\nNot later than 180 days after the date of the first meeting of the review panel, the review panel shall submit to the Administrator and the appropriate committees of Congress a report containing the findings and recommendations regarding the matters listed in paragraph (2) that are endorsed by a majority of the appointed members of the review panel.\n**(B) Dissenting views**\nIn submitting the report under subparagraph (A), the review panel shall append to such report the dissenting views of any individual appointed member or group of appointed members of the review panel regarding the findings or recommendations of the review panel.\n**(C) Publication**\nNot later than 5 days after receiving the report under subparagraph (A), the Administrator shall publish such report, including any dissenting views appended to the report, on the website of the FAA.\n**(D) Termination**\nThe review panel shall terminate upon the submission of the report under subparagraph (A).\n**(6) Administrative provisions**\n**(A) Access to information**\n**(i) In general**\nThe review panel shall have the authority to perform the following actions if a majority of the appointed members of the review panel consider each action necessary and appropriate:\n**(I)**\nEntering onto the premises of the FAA for access to and inspection of records or other purposes.\n**(II)**\nNotwithstanding any other provision of law, except as provided in clause (ii), accessing and inspecting de-identified, but otherwise unredacted, records directly necessary for the completion of the review panel\u2019s work under this section that are in the possession of the FAA.\n**(III)**\nInterviewing employees of the FAA as necessary for the review panel to complete its work.\n**(ii) Non-federal government members**\nMembers of the review panel who are not officers or employees of the Federal Government shall only have access to, and be allowed to inspect, information provided to the FAA pursuant to section 40123 of title 49, United States Code, and part 193 of title 14, Code of Federal Regulations, in a de-identified form.\n**(B) Nondisclosure of confidential information**\n**(i) Nondisclosure for non-federal government members**\n**(I) Non-federal government participants**\nPrior to participating on the review panel, each individual serving on the review panel representing a non-Federal entity shall execute an agreement with the Administrator in which the individual shall be prohibited from disclosing at any time, except as required by law, to any person, foreign or domestic, any non-public information made available to the panel under subparagraph (A).\n**(II) Federal government participants**\nFederal officers or employees serving on the review panel as representatives of the Federal Government and subject to the requirement to protect confidential information (including proprietary information and trade secrets under section 1905 of title 18, United States Code) shall not be required to execute agreements under this clause.\n**(ii) Protection of information**\nInformation that is obtained or reviewed by the review panel shall not constitute a waiver of the protections applicable to the information under section 552 of title 5, United States Code (commonly referred to as the Freedom of Information Act ). Members of the review panel shall protect such information to the extent required under applicable law.\n**(iii) Protection of proprietary information and trade secrets**\nMembers of the review panel shall protect proprietary information, trade secrets, and other information otherwise exempt under section 552 of title 5, United States Code, to the extent permitted under applicable law.\n**(7) Inapplicability of FACA**\nThe review panel shall not be subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ).\n**(8) Congressional briefings**\nNot later than 180 days after the submission of the recommendations under paragraph (4), and every 90 days thereafter, the Administrator shall report to the appropriate committees of Congress on the status of any ongoing actions in response to such recommendations, including the status of implementation of each of the recommendations of the review panel, if any, with which the Administrator concurs.\n##### (b) Non-Concurrence with recommendations\nNot later than 6 months after submission of the recommendations under subsection (a)(4), with respect to each recommendation of the review panel with which the Administrator does not concur, if any, the Administrator shall publish on the website of the FAA and submit to the appropriate committees of Congress a detailed explanation for such determination.\n##### (c) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) Appropriate committees of congress**\nThe term appropriate committees of Congress means the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives.\n**(3) FAA**\nThe term FAA means the Federal Aviation Administration.\n**(4) ICAO**\nThe term ICAO means the International Civil Aviation Organization.\n**(5) SMS**\nThe term SMS means a safety management system.",
      "versionDate": "2026-01-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-07T15:44:41Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-04-07T15:44:33Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2026-04-07T15:23:01Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-07T15:28:06Z"
          },
          {
            "name": "Employee performance",
            "updateDate": "2026-04-07T15:27:41Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-04-07T15:27:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-07T15:45:06Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-07T15:28:12Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2026-04-07T15:23:24Z"
          },
          {
            "name": "Travel and tourism",
            "updateDate": "2026-04-07T15:23:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-04T15:17:03Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3700is.xml"
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
      "title": "FAA SMS Compliance Review Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAA SMS Compliance Review Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-02T22:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an expert review panel to make recommendations for a comprehensive agency-wide safety management system at the FAA.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-02T22:03:15Z"
    }
  ]
}
```
