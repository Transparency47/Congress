# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3355
- Title: National Strategy for Combating Scams Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3355
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-15T07:07:46Z
- Update date including text: 2026-01-15T07:07:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3355",
    "number": "3355",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "National Strategy for Combating Scams Act of 2025",
    "type": "S",
    "updateDate": "2026-01-15T07:07:46Z",
    "updateDateIncludingText": "2026-01-15T07:07:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:23:10Z",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "AZ"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3355is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3355\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mrs. Gillibrand (for herself, Mr. Scott of Florida , Mr. Kelly , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a national strategy for combating scams, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Strategy for Combating Scams Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMore than 4 in 10 individuals in the United States, an estimated 141,500,000 adults, say they have lost money to scams or had sensitive information obtained and used fraudulently.\n**(2)**\nConsumers reported losing more than $12,000,000,000 to fraud in 2024, a 25 percent increase over the prior year, with imposter scams being the most commonly reported scam category.\n**(3)**\nCriminals are increasingly using Generative Artificial Intelligence to conduct scams, including hyper-realistic voice deepfakes to manipulate victims.\n**(4)**\nScams harm all people of the United States, but can particularly affect older adults by harming their mental health and by forcing them to live with fewer resources.\n**(5)**\nThe Government Accountability Office found that there are at least 13 agencies engaged in a range of activities relating to countering scams, all of which have their own mandate and authorities and are largely carrying out their activities independently.\n**(6)**\nTo improve the ability of Federal agencies to coordinate and target efforts to counter scams, the Government Accountability Office has recommended that the Federal Bureau of Investigations lead an effort to develop a National Strategy for Combating Scams.\n#### 3. National Strategy for Combating Scams\n##### (a) Establishment of working group\nNot later than 90 days after the date of enactment of this Act, the Director of the Federal Bureau of Investigation shall assemble a working group to develop a National Strategy for Combating Scams, in coordination with the heads of each of the following:\n**(1)**\nThe Federal Trade Commission.\n**(2)**\nThe Consumer Financial Protection Bureau.\n**(3)**\nThe Department of Health and Human Services.\n**(4)**\nThe Department of State.\n**(5)**\nThe Federal Deposit Insurance Corporation.\n**(6)**\nThe Federal Reserve Board.\n**(7)**\nThe Financial Crimes Enforcement Network.\n**(8)**\nThe Department of Homeland Security.\n**(9)**\nThe National Credit Union Administration.\n**(10)**\nThe Office of the Comptroller of Currency.\n**(11)**\nThe Office of the United States Attorney.\n**(12)**\nThe United States Secret Service.\n**(13)**\nThe Department of the Treasury.\n**(14)**\nThe Federal Communications Commission.\n**(15)**\nThe Securities and Exchange Commission.\n**(16)**\nThe Commodities Futures Trading Commission.\n**(17)**\nThe Social Security Administration.\n**(18)**\nAny other Federal Department or agency, as determined appropriate.\n##### (b) Development of National Strategy for Combating Scams\nThe working group established pursuant to subsection (a) shall develop a National Strategy for Combating Scams that\u2014\n**(1)**\nincorporates feedback from community stakeholders, including\u2014\n**(A)**\nsurvivors of scams, and groups that represent survivors of scams;\n**(B)**\nolder adults and groups that represent older adults;\n**(C)**\nindividuals with disabilities and groups that represent individuals with disabilities;\n**(D)**\nFederal, State, and local prosecutors and law enforcement officials with expertise in scams, and groups that represent such prosecutors and law enforcement officials;\n**(E)**\nbusiness and non-profit organizations that play a role in preventing and addressing scams, including telecommunications, financial, social media, retail, and technology companies, and groups that represent such businesses and non-profit organizations;\n**(F)**\nexperts on human behavior and scam prevention;\n**(G)**\nAdult Protective Services agencies, and groups that represent them;\n**(H)**\nArea Agencies on Aging, and groups that represent them;\n**(I)**\nState, local, and Tribal government officials, and groups that represent State and local government officials; and\n**(J)**\nany other community stakeholders, as determined appropriate by the working group;\n**(2)**\nestablishes a definition of scam , for use in the National Strategy and by the Federal Bureau of Investigation, the Federal Trade Commission, and the Consumer Financial Protection Bureau, the establishment of which includes\u2014\n**(A)**\nan analysis explaining the reasons the working group selected the definition; and\n**(B)**\nan evaluation of whether agencies other than the Federal Bureau of Investigation, the Federal Trade Commission, and the Consumer Financial Protection Bureau FBI should adopt the definition, including an analysis of the barriers or unintended consequences of doing so;\n**(3)**\nevaluates the risks from scams, including an analysis of threats and vulnerabilities, health and financial risks to scam survivors, risks to national and economic security, and the proper Federal response to scams;\n**(4)**\nevaluates methods for preventing scams, including evidence-based best practices that can be implemented and measured by the Federal Government, State, local, and Tribal governments, businesses, non-profit organizations, community members, and family members of those at risk of being scammed;\n**(5)**\ndefines agency roles, responsibilities, and authorities for preventing and combating scams;\n**(6)**\nanalyzes maintaining a single, government-wide estimate of scams perpetrated and the dollar losses associated with them, including incidents not reported, including either\u2014\n**(A)**\na plan for developing and maintaining such an estimate; or\n**(B)**\nan analysis of the barriers preventing the development of such an estimate and the legislative, regulatory, or administrative changes that could eliminate those barriers;\n**(7)**\nformulates a plan to\u2014\n**(A)**\nensure coordinated, consistent, and accessible consumer complaint reporting for scams across Federal agencies, including complaint reporting that is accessible for individuals with disabilities;\n**(B)**\nidentify duplication in tasks and responsibilities between agencies and establish deconfliction procedures for overlapping jurisdictional authorities to improve coordination and collaboration;\n**(C)**\nensure harmonized, adequate, timely, and accurate data collection and data aggregation on scams across Federal agencies, including ways to\u2014\n**(i)**\nbetter collect data and encourage reporting on scams;\n**(ii)**\nbetter identify scams;\n**(iii)**\nconsistently collect data on the types of scams, dollar losses from scams, payment methods used for scams, and other data, as appropriate;\n**(iv)**\npromote Federal law enforcement data interoperability and intelligence gathering across data collection platforms; and\n**(v)**\nmodernize law enforcement data and reporting, including through the use of artificial intelligence and other innovative technology to enhance data synthesis;\n**(D)**\nincrease coordination between Federal and private sector efforts, including efforts by businesses and non-profits, to prevent scams by\u2014\n**(i)**\nfacilitating and coordinating the rapid sharing of data by private sector businesses (including technology companies, banks, and telecommunication companies) necessary to the investigation of scams by law enforcement officials;\n**(ii)**\nauthenticating legitimate and blocking scam-related transactions and communications; and\n**(iii)**\ncoordinating preemptive enforcement and takedown actions;\n**(E)**\nestablish coordinated rapid response protocols that provide individuals with timely, accurate warnings and prevention guidance through trusted channels, ensuring that scam threats are identified quickly and communicated effectively to the public;\n**(F)**\nincrease coordination between Federal, State, local, and Tribal government efforts to prevent and combat scams, including analyzing the feasibility of the creation of elder justice task forces within local governments;\n**(G)**\ncoordinate efforts to address complex and multifaceted scams that cross jurisdictional boundaries; and\n**(H)**\nmonitor and evaluate the effectiveness of the implementation of strategies recommended in the National Strategy for Combating Scams;\n**(8)**\nevaluate ways for the Federal Government to partner with State, local, and Tribal law enforcement agencies, financial institutions, telecom carriers, technology companies, and other entities determined appropriate to support victim recovery, including providing clear accessible resources for assistance and redress;\n**(9)**\nenhance coordination with foreign countries to combat large-scale scams originating abroad that target persons in the United States to improve cross-border enforcement;\n**(10)**\nanalyzes the legislative, regulatory, or administrative changes needed to carry out the National Strategy for Combating Scams and enable a comprehensive and coordinated Federal response to scams;\n**(11)**\nidentifies the resources needed to prevent and combat scams and implement the National Strategy for Combating Scams; and\n**(12)**\naddresses any other topic relating to the promotion of a coordinated national response to scams, as determined appropriate by the working group.\n##### (c) Submission and publication\nNot later than 2 years after the establishment of the working group under subsection (a), the working group shall\u2014\n**(1)**\nsubmit the National Strategy for Combating Scams developed under subsection (b) to the Special Committee on Aging of the Senate , the Committee on the Judiciary of the Senate , and the Committee on the Judiciary of the House of Representatives ; and\n**(2)**\nmake the National Strategy for Combating Scams publicly available, including on a publicly accessible website.\n##### (d) Updates\n**(1) In general**\nFollowing the publication of the National Strategy for Combating Scams under paragraph (c), not less frequently than once every 5 years, the working group established pursuant to subsection (a) shall update such publication, including by\u2014\n**(A)**\ncollecting and incorporating new feedback from community stakeholders; and\n**(B)**\nupdating the definition of scam , as appropriate.\n**(2) Submission and publication**\nNot later than 30 days after each update under paragraph (1), the working group established pursuant to subsection (a)shall\u2014\n**(A)**\nsubmit the updated National Strategy for Combating Scams to the Special Committee on Aging of the Senate , the Committee on the Judiciary of the Senate , and the Committee on the Judiciary of the House of Representatives ; and\n**(B)**\nmake the updated National Strategy for Combating Scams publicly available, including on a publicly accessible website.\n#### 4. Adoption of common definition of scam\n##### (a) In general\nNot later than 1 year after the publication of the National Strategy for Combating Scams under section 3(c), the Federal Bureau of Investigation, the Federal Trade Commission, and the Consumer Financial Protection Bureau shall adopt the common definition of scam recommended in the National Strategy for Combating Scams.\n##### (b) Updates to definition\nIf, pursuant to section 3(d), the working group updates the definition of scam in an updated National Strategy for Combating Scams, the Federal Bureau of Investigation, the Federal Trade Commission, and the Consumer Financial Protection Bureau shall adopt the updated common definition of scam not later than 1 year after such update.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Energy and Commerce, and Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6425",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "National Strategy for Combating Scams Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2026-01-07T17:31:22Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3355is.xml"
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
      "title": "National Strategy for Combating Scams Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Strategy for Combating Scams Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a national strategy for combating scams, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:15Z"
    }
  ]
}
```
