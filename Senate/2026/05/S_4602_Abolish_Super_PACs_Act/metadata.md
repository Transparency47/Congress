# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4602
- Title: Abolish Super PACs Act
- Congress: 119
- Bill type: S
- Bill number: 4602
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-30T04:53:26Z
- Update date including text: 2026-05-30T04:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4602",
    "number": "4602",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Abolish Super PACs Act",
    "type": "S",
    "updateDate": "2026-05-30T04:53:26Z",
    "updateDateIncludingText": "2026-05-30T04:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T19:48:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4602is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4602\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Sanders introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to place reasonable limits on contributions to Super PACs which make independent expenditures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Abolish Super PACs Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds as follows:\n**(1)**\nContribution limits to political action committees (PACs), including those that make independent expenditures, help secure elections by limiting both the risk of corruption and the risk that significant contributions will create the appearance of corruption.\n**(2)**\nSince contribution limits on super PACs were lifted in 2010, the number, influence, and wealth of super PACs have exploded. Obtaining millions or billions of dollars in contributions to super PACs is now critical to the success of Federal candidates\u2019 campaigns.\n**(3)**\nAs the influence of super PACs grows, so does the likelihood that they will serve as a conduit for corrupt agreements between contributor and candidate, whose communications are not subject to coordination limitations.\n**(4)**\nBetween 2008 and 2020, the amount of independent expenditures increased more than 700 percent, and in 2024, more than $4.48 billion in independent expenditures were spent on United States elections. The money for these expenditures largely came from contributions to 2,459 registered super PACs.\n**(5)**\nIn 2012, the first modern elections for Federal office held without contribution limits to super PACs, the top 1 percent of all individual super PAC contributors contributed 76.76 percent of all individual super PAC contributions, and that percentage rose to 96.94 percent in 2024. Recent elections have been influenced by individual contributors who gave more than $100 million to super PACs.\n**(6)**\nAs bribery laws have long recognized, unlawful quid pro quo exchanges can occur where the bribe is funneled into a third party, such as a super PAC. See, e.g., section 201 of title 18, United States Code; U.S. v. Menendez, 291 F. Supp. 606, 621\u201323 (D. N.J. 2018). Law enforcement in several States have prosecuted cases that involve bribes directed to super PACs. However, bribery is notoriously difficult to prosecute, and these laws do not adequately protect American voters from corruption.\n**(7)**\nWithout reasonable limitations on contributions, super PACs create an appearance of corruption. A bipartisan majority of Americans believe that large super PAC contributions are made in exchange for political favors, and that corruption is pervasive in the Federal Government. This is, as the Supreme Court recognized in Buckley v. Valeo, disastrous to confidence in the system of representative government 424 U.S. 1, 27 (1976).\n**(8)**\nPlacing limits on super PAC contributions will also lessen the risk of foreign interference in United States elections, making it more difficult for foreign entities to funnel contributions to super PACs via third-party contributors.\n**(9)**\nSpeechNow.org v. FEC, 599 F.3d 686 (D.C. Cir. 2010), the appellate court case that voided existing contribution limits to super PACs, wrongly treated contributions as expenditures and wrongly assumed that because uncoordinated independent expenditures cannot give rise to quid pro quo corruption, that contributions to independent expenditure committees similarly cannot give rise to corruption. But they can and do.\n**(10)**\nIn the 14 years since SpeechNow unleashed billions of dollars in unregulated contributions, super PACs have obtained unprecedented wealth and value to candidate campaigns and can facilitate vast, nearly untraceable corrupt transactions.\n**(11)**\nBecause Super PACs have become uniquely important to candidate campaigns and can accept millions and even hundreds of millions of dollars from single entities, candidates and contributors have reason and opportunity to guide corrupt contributions into super PACs, establishing a significant risk of corruption and creating an appearance of corruption that undermines the public\u2019s faith in their representatives and our political system.\n**(12)**\nReasonable limits on contributions to super PACs are lawful and necessary to protect American democracy and American voters.\n##### (b) Purpose\nIt is the purpose of this Act\u2014\n**(1)**\nto limit the risk of corrupt agreements between candidates and contributors by placing reasonable limits on contributions to political action committees that make independent expenditures;\n**(2)**\nto limit the appearance of corruption created by uncapped contributions to political action committees that make independent expenditures; and\n**(3)**\nto restore the public\u2019s faith in our elections.\n#### 3. Limitation on contributions to independent expenditure committees\n##### (a) Limitations\nSection 315(a)(1)(C) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30116(a)(1)(C) ) is amended by striking to any other political committee and inserting to an independent expenditure committee or any other political committee .\n##### (b) Definition\nSection 301 of such Act ( 52 U.S.C. 30101 ) is amended by adding at the end the following:\n(27) Independent expenditure committee (A) In general The term independent expenditure committee means a political committee which\u2014 (i) makes independent expenditures aggregating $5,000 or more during a calendar year; or (ii) makes contributions to other independent expenditure committees aggregating $5,000 or more during a calendar year. (B) Treatment of separate accounts The term independent expenditure committee includes an account of a political committee which is established for the purpose of making independent expenditures or contributions to other committees making independent expenditures. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to contributions and independent expenditures made during the first calendar year which begins after the date of the enactment of this Act and each succeeding calendar year.",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4602is.xml"
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
      "title": "Abolish Super PACs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Abolish Super PACs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Election Campaign Act of 1971 to place reasonable limits on contributions to super PACs which make independent expenditures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T04:48:25Z"
    }
  ]
}
```
