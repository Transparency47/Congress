# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3428
- Title: SAFE Crypto Act
- Congress: 119
- Bill type: S
- Bill number: 3428
- Origin chamber: Senate
- Introduced date: 2025-12-10
- Update date: 2026-05-12T11:03:32Z
- Update date including text: 2026-05-12T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in Senate
- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-10: Introduced in Senate

## Actions

- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3428",
    "number": "3428",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "SAFE Crypto Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:32Z",
    "updateDateIncludingText": "2026-05-12T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-10",
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
            "date": "2025-12-10T22:24:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-10T22:24:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3428is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3428\nIN THE SENATE OF THE UNITED STATES\nDecember 10, 2025 Mr. Moran (for himself and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a Task Force for Recognizing and Averting Cryptocurrency Scams, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Agency Frameworks for Enforcement of Cryptocurrency Act or the SAFE Crypto Act .\n#### 2. Definitions\nIn this Act:\n**(1) Digital asset; digital asset service provider; permitted payment stablecoin issuer**\nThe terms digital asset ; digital asset service provider ; and permitted payment stablecoin issuer have the meanings given those terms in section 2 of the GENIUS Act ( 12 U.S.C. 5901 ), respectively.\n**(2) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(3) Task Force**\nThe term Task Force means the Task Force on Cryptocurrency Scams established under section 3(a).\n#### 3. Task Force on Cryptocurrency Scams\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a task force, to be known as the Task Force for Recognizing and Averting Cryptocurrency Scams.\n##### (b) Membership\n**(1) Composition**\nThe Task Force shall be chaired by the Secretary, or a designee thereof, and shall consist of the following individuals, or the designees of these individuals:\n**(A)**\nThe Attorney General.\n**(B)**\nThe Director of the Financial Crimes Enforcement Network.\n**(C)**\nThe Director of the United States Secret Service.\n**(D)**\nThe head of any other relevant Federal department or agency, as determined by the Secretary, in consultation with the Task Force.\n**(E)**\nRepresentatives of permitted payment stablecoin issuers.\n**(F)**\nRepresentatives of digital asset service providers.\n**(G)**\nRepresentatives of digital asset custodians.\n**(H)**\nRepresentatives of blockchain intelligence providers.\n**(I)**\nRepresentatives of victims, scam support networks, or other relevant consumer protection stakeholders.\n**(J)**\nRepresentatives of Federal, State, and local law enforcement.\n**(K)**\nRepresentatives of any other industries, as determined necessary by the Secretary.\n**(L)**\nRepresentatives from 1 or more State bank regulatory authorities.\n**(2) Term of appointment**\nThe term of a member of the Task Force shall continue until the termination of the Task Force.\n**(3) Vacancy**\nAny vacancy occurring in the membership of the Task Force shall be filled in the same manner in which the original appointment was made.\n##### (c) Purposes\nThe purposes of the Task Force include the following:\n**(1) Scam detection and prevention**\nThe Task Force shall examine current trends and developments in the financial grooming scams involving digital assets, identify effective methods for preventing such scams, and issue recommendations to enhance efforts to identify and prevent such activities.\n**(2) Cross-sector approach**\nThe Task Force shall adopt a cross-sector approach to ensure its recommendations reflect the full scope of the issue, given that scams impact individuals across jurisdictions and a wide range of industries, including financial services, telecommunications, and technology.\n**(3) Stakeholder insight**\nThe Task Force shall include representation from\u2014\n**(A)**\nstakeholders with direct experience supporting victims of scams (including individuals forced to engage in the scams and individuals impacted by the scams); and\n**(B)**\nindustry participants with insight into\u2014\n**(i)**\nthe organized crime networks perpetrating the scams;\n**(ii)**\ndigital asset ATMs; and\n**(iii)**\nprevention strategies, including following the money to detect, deter, and dismantle the organized crime networks.\n**(4) Information sharing and interdiction networks**\nThe Task Force, in coordination with relevant Federal agencies, is encouraged to promote participation by digital asset service providers and permitted payment stablecoin issuers in public-private, real-time information sharing and interdiction networks designed to detect, disrupt, and prevent the off-ramping of funds associated with scams, fraud, and other illicit activities.\n**(5) Enhanced asset recovery mechanisms**\nThe Task Force shall work with permitted payment stablecoin issuers to ensure that the permitted payment stablecoin issuers maintain and use technical capabilities to freeze, seize, burn, or reissue digital assets determined to be proceeds of scams or other unlawful conduct, consistent with applicable law and due process protections.\n##### (d) Meetings\nThe Task Force shall meet not less than 3 times during the 1-year period beginning on the date of enactment of this Act, and thereafter at such times and places, and by such means, as the Chair of the Task Force determines to be appropriate, which may include the use of remote conference technology.\n##### (e) Duties\nThe duties of the Task Force shall include\u2014\n**(1)**\nevaluating opportunities to use data collected by the Internet Crime Complaint Center database of the Federal Bureau of Investigation and the fraud reporting database of the Federal Trade Commission;\n**(2)**\nevaluating best practices for combating methods (such as financial grooming scams, Ponzi schemes, money laundering, organized crime schemes, fraudulent Initial Coin Offerings, and rug pulls) used by scammers, including means of identifying, communicating with, and exploiting victims;\n**(3)**\nassessing how international jurisdictions have tried to prevent scams involving digital assets;\n**(4)**\nidentifying and reviewing current methods used to scam individuals, including users and consumers, using digital asset intermediaries;\n**(5)**\ndetermining a strategy for education programs that better equip individuals, including consumers, to identify, avoid, and report digital asset scam attempts to the appropriate law enforcement or government authorities;\n**(6)**\ncoordinating efforts to ensure perpetrators of scams involving digital assets can be identified and pursued by law enforcement;\n**(7)**\nconsulting with other relevant stakeholders, including State, local, and Tribal agencies and financial services providers;\n**(8)**\ndetermining whether any additional Federal legislation and full-time equivalents would be beneficial for law enforcement and industry in mitigating scams involving digital assets; and\n**(9)**\nworking with international governments and law enforcement agencies to combat digital asset scams, including by targeting the organized crime networks perpetrating scams, originating abroad.\n##### (f) Compensation\nEach member of the Task Force shall serve without compensation, other than compensation to which entitled as an employee of the United States, as the case may be.\n##### (g) Report\n**(1) In general**\nNot later than 1 year after the date on which the Secretary establishes the Task Force, the Task Force shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate , the Committee on Agriculture, Nutrition, and Forestry of the Senate , the Committee on Financial Services of the House of Representatives , and the Committee on Agriculture of the House of Representatives and make publicly available online a report detailing\u2014\n**(A)**\nthe results of the reviews and evaluations of the Task Force under subsection (e);\n**(B)**\nthe strategy identified under subsection (e);\n**(C)**\nany legislative, regulatory, or personnel recommendations that would enhance the ability to detect and prevent scams involving digital assets described in subsection (e); and\n**(D)**\nrecommendations to enhance cooperation among Federal, State, local, and Tribal authorities in the investigation and prosecution of scams and other financial crimes, including harmonizing data collection, improving data sharing processes, improving reporting mechanisms and streams, estimating the number of complaints and consumers affected, and evaluating the effectiveness of anti-scam training programs.\n**(2) Annual updates**\nAfter submitting an initial report required under paragraph (1), the Task Force shall, on an annual basis, submit to the Committee on Banking, Housing, and Urban Affairs of the Senate , the Committee on Agriculture, Nutrition, and Forestry of the Senate , the Committee on Financial Services of the House of Representatives , and the Committee on Agriculture of the House of Representatives and make publicly available online an updated version of the report.\n##### (h) Applicable law\nChapter 4 of title 5, United States Code, shall not apply to the Task Force.\n##### (i) Sunset\nThe Task Force shall terminate on the date that is 3 years after the date on which the Task Force submits the report required under subsection (g)(1).",
      "versionDate": "2025-12-10",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-08T19:46:01Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3428is.xml"
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
      "title": "SAFE Crypto Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Crypto Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Agency Frameworks for Enforcement of Cryptocurrency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Task Force for Recognizing and Averting Cryptocurrency Scams, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:23Z"
    }
  ]
}
```
