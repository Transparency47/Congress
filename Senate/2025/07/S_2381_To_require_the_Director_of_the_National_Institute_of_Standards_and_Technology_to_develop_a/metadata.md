# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2381?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2381
- Title: PROACTIV Artificial Intelligence Data Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2381
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2025-12-02T12:03:45Z
- Update date including text: 2025-12-02T12:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2381",
    "number": "2381",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "PROACTIV Artificial Intelligence Data Act of 2025",
    "type": "S",
    "updateDate": "2025-12-02T12:03:45Z",
    "updateDateIncludingText": "2025-12-02T12:03:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T19:38:40Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NJ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2381is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2381\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Cornyn (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Director of the National Institute of Standards and Technology to develop a framework for detecting, removing, and reporting child pornography in datasets used to train artificial intelligence systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Recurring Online Abuse of Children Through Intentional Vetting of Artificial Intelligence Data Act of 2025 or the PROACTIV Artificial Intelligence Data Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given that term in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. note prec. 4061).\n**(2) Artificial intelligence developer**\nThe term artificial intelligence developer means a person who designs, codes, or produces an artificial intelligence system and makes such system commercially available, whether for profit or not.\n**(3) Artificial Intelligence Deployer**\n.The term artificial intelligence deployer means a person who integrates an artificial intelligence system into the products or services of the person and makes those products or services commercially available, whether for profit or not.\n**(4) Artificial intelligence user**\nThe term artificial intelligence user means a person who uses an artificial intelligence system for a purpose other than personal noncommercial activity.\n**(5) Child pornography**\nThe term child pornography has the meaning given that term in section 2256 of title 18, United States Code.\n**(6) Covered dataset**\nThe term covered dataset means a set of data that\u2014\n**(A)**\nis collected for the purpose of training an artificial intelligence system; and\n**(B)**\nwas created using automated data crawlers or data scraping tools, whether or not directed by a human operator.\n**(7) Data collector**\nThe term data collector means any person who specializes in collecting, preparing, cleaning, labeling, transforming for algorithmic compatibility, and organizing large amounts of data for the purpose of training an artificial intelligence system.\n**(8) Director**\nThe term Director means the Director of the National Institute of Standards and Technology.\n#### 3. Development of framework on detecting, removing, and reporting child pornography in certain datasets\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Director shall, in collaboration with such other Federal agencies and public and private sector organizations as the Director considers appropriate, including the National Science Foundation, the National Center for Missing and Exploited Children, and the Department of Justice, develop and publish a voluntary framework for detecting, removing, and reporting child pornography in covered datasets.\n##### (b) Contents\nThe Director shall ensure that the framework published under subsection (a) provides to artificial intelligence developers and to data collectors guidelines, best practices, methodologies, procedures, and processes\u2014\n**(1)**\nto detect any child pornography in covered datasets;\n**(2)**\nto remove any child pornography from covered datasets; and\n**(3)**\nto regularly report to Federal, State, or local law enforcement and the National Center for Missing and Exploited Children any child pornography detected in covered datasets.\n##### (c) Limitation\nThe framework published under subsection (a) shall apply to persons who are artificial intelligence developers and to data collectors, and not to persons who are solely artificial intelligence deployers or artificial intelligence users.\n##### (d) Stakeholder outreach\nIn developing the framework issued under subsection (a), the Director shall\u2014\n**(1)**\nsolicit input from\u2014\n**(A)**\ninstitutions of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ));\n**(B)**\nany Federal agency the Director considers relevant;\n**(C)**\ncivil society and nonprofit organizations;\n**(D)**\nartificial intelligence developers and artificial intelligence deployers;\n**(E)**\nFederal laboratories (as defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )); and\n**(F)**\nany other such stakeholder the Director considers appropriate; and\n**(2)**\nprovide an opportunity for public comment on the guidelines, best practices, methodologies, procedures, and processes developed as part of the framework.\n##### (e) Research\nThe Director of the National Science Foundation, in coordination with the heads of other relevant Federal agencies, as determined by such Director, shall support research into innovative approaches to detecting, removing, and reporting child pornography from covered datasets, including research conducted through the Directorate for Technology, Innovation, and Partnerships.\n#### 4. Limited liability for detecting, removing, and reporting child pornography\n##### (a) In general\nExcept as provided in subsection (b), no cause of action shall lie or be maintained in any court against an artificial intelligence developer or data collector, and such action shall be promptly dismissed, for the detecting, removing, or reporting of child pornography in covered datasets that is conducted in accordance with the framework issued by the Director under section 3(a).\n##### (b) Intentional, reckless, grossly negligent, or other misconduct\nSubsection (a) shall not apply to a cause of action for detecting, removing, or reporting child pornography in covered datasets if the artificial intelligence developer or data collector\u2014\n**(1)**\nengaged in intentional misconduct;\n**(2)**\nacted, or failed to act\u2014\n**(A)**\nwith actual malice;\n**(B)**\nwith reckless disregard to a substantial risk of causing injury without legal justification; or\n**(C)**\nwith gross negligence; or\n**(3)**\nengaged in any activity that violates section 2251 of title 18, United States Code.\n##### (c) Rule of construction\nNothing in this Act shall be construed to affect the protections and obligations of section 2258A of title 18, United States Code.",
      "versionDate": "2025-07-22",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-09-12T16:51:12Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2025-09-12T16:50:59Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-12T16:56:07Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-09-12T16:51:06Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2025-09-12T16:56:13Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-09-12T17:00:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-12T14:49:06Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2381is.xml"
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
      "title": "PROACTIV Artificial Intelligence Data Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROACTIV Artificial Intelligence Data Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Recurring Online Abuse of Children Through Intentional Vetting of Artificial Intelligence Data Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the National Institute of Standards and Technology to develop a framework for detecting, removing, and reporting child pornography in datasets used to train artificial intelligence systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:25Z"
    }
  ]
}
```
