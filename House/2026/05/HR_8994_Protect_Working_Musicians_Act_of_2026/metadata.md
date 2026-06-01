# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8994?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8994
- Title: Protect Working Musicians Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8994
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-30T08:06:09Z
- Update date including text: 2026-05-30T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8994",
    "number": "8994",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Protect Working Musicians Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:09Z",
    "updateDateIncludingText": "2026-05-30T08:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-05-21T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "TN"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "TX"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8994ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8994\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2026 Ms. Ross (for herself, Mr. Cohen , and Mr. Doggett ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo empower independent music creator owners to collectively negotiate with dominant online platforms regarding the terms on which their music may be distributed.\n#### 1. Short title\nThis Act may be cited as the Protect Working Musicians Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMusic is a cultural treasure and a unique source of spiritual inspiration, emotional comfort, community connection, and joy. It is also a powerful economic driver that directly and indirectly supports nearly 2 million American jobs and almost $150 billion in annual economic activity.\n**(2)**\nA healthy music ecosystem is a fundamental bedrock for a healthy society.\n**(3)**\nFair and competitive markets for the use and licensing of recorded music are integral to a healthy music ecosystem.\n**(4)**\nAs music distribution has moved online, the market for use and licensing has become distorted and imbalanced. The largest Dominant Online Music Distribution Platforms use their market power to distort legal requirements and force music creators into licensing agreements that do not reflect market value. Those agreements essentially dictate a price to music creators. If music creators do not agree to licensing terms, the online platforms profit from unlicensed uploads of music anyway.\n**(5)**\nThese platforms game the system created by the Digital Millennium Copyright Act, which allows dominant online platforms to ignore and profit from unlicensed use of music and places the responsibility for finding each and every instance of unlicensed use of music on music creators. This notice and takedown scheme has been described as a gigabit-speed game of whack-a-mole.\n**(6)**\nThe trade association for the major record labels spends millions of dollars engaged in this effort which it says has grown to be largely useless. The trade association for the independent record labels agrees, calling it a dysfunctional relic .\n**(7)**\nAn effort that is largely useless for major and independent record labels is an exercise in futility for Independent Music Creator Owners\u2014those who own the copyrights and market their work themselves. Independent Music Creator Owners lack the economic, legal, and political resources to stand up to the Dominant Online Music Distribution Platforms and have no way to meaningfully negotiate fair licensing rates for their work.\n**(8)**\nThat power imbalance means that Independent Music Creator Owners are forced to take whatever terms dominant online platforms offer for their work. If they decline, the platforms simply ignore them since in most cases lacking access to any single artists\u2019 work does not present a threat to the platforms\u2019 overall attractiveness to consumers.\n**(9)**\nThis imbalance has decimated careers in music at an untold cost to our society and culture. Multi Grammy-award winning musician Rosanne Cash recently lamented: I see young musicians give up their missions and dreams all the time because they can\u2019t make a living.\n**(10)**\nThe antitrust laws were intended to and do provide important economic and civic benefits.\n**(11)**\nA central purpose of these laws is to promote, protect, and strengthen fair and open markets, including those for music.\n**(12)**\nWhile antitrust exemptions are generally disfavored, should the application of the antitrust laws ever be applied in a manner that conflicts with their purpose\u2014such as protecting the online marketplace for creative works\u2014it is the duty and prerogative of the Congress to resolve the conflict.\n#### 3. Safe harbor for certain collective negotiations\n##### (a) Definitions\nFor purposes of this section:\n**(1)**\nThe term antitrust laws has the meaning given such term in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ), and includes\u2014\n**(A)**\nsection 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that such section applies to unfair methods of competition; and\n**(B)**\nany State law, rule, or regulation that prohibits or penalizes the conduct described in, or is otherwise inconsistent with, subsection (b) of this section.\n**(2)**\nThe term Dominant Online Music Distribution Platform means any entity that\u2014\n**(A)**\noperates an app, website or other online service that is used by members of the public to listen to sound recordings, whether via a digital audio transmission, an audio-visual presentation, or any other means;\n**(B)**\nhas annual revenues related to the distribution of music of more than $100 million; and\n**(C)**\nis not eligible for a license under section 114(d)(2) of title 17 of the United States Code.\n**(3)**\nThe term generative artificial intelligence means an artificial intelligence system that is capable of generating novel text, video, images, audio, and other media based on prompts or other forms of data provided by a person.\n**(4)**\nThe term Individual Music Creator Owner means any musician or group of musician, producers, mixers, and sound engineers that\u2014\n**(A)**\nowns the copyrights to one or more sound recordings created by the musician or group of musicians, producers, and sound engineers; and\n**(B)**\neither:\n**(i)**\nhas earned less than $1,000,000 in licensing revenues associated with these copyrights in the prior year; or\n**(ii)**\nqualifies as a small business under the Office of Management and Budget North American Industry Classification System (NAICS) code 512250.\n##### (b) Limitation of liability\nAn Individual Music Creator Owner shall not be held liable under the antitrust laws for agreeing with other Individual Music Creator Owners to collectively negotiate music licensing terms with a Dominant Online Music Distribution Platform or a company engaged in development or deployment of generative artificial intelligence, or agreeing with other Individual Music Creator Owners to collectively refuse to license their music to a Dominant Online Music Distribution Platform or a company engaged in development or deployment of generative artificial intelligence, if\u2014\n**(1)**\nthe negotiations are not limited to price, are nondiscriminatory as to similarly situated independent creator/owners;\n**(2)**\nthe coordination among Independent Music Creator Owners is directly related to and reasonably necessary for negotiations with a Dominant Online Music Distribution Platform that are otherwise consistent with the operation of the Antitrust laws; and\n**(3)**\nthe negotiations do not involve any person that is not an Independent Music Creator Owner or a Dominant Online Music Distribution Platform.\n##### (c) Rule of construction\nExcept as provided in this Act, this Act shall not be construed to modify, impair, or supersede the operation of the antitrust laws.",
      "versionDate": "2026-05-21",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8994ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protect Working Musicians Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Working Musicians Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To empower independent music creator owners to collectively negotiate with dominant online platforms regarding the terms on which their music may be distributed.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:27Z"
    }
  ]
}
```
