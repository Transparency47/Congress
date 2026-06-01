# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4586?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4586
- Title: Blocking CCP Spy Tech Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4586
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-29T07:23:31Z
- Update date including text: 2026-05-29T07:23:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4586",
    "number": "4586",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Blocking CCP Spy Tech Act of 2026",
    "type": "S",
    "updateDate": "2026-05-29T07:23:31Z",
    "updateDateIncludingText": "2026-05-29T07:23:31Z"
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
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
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
          "date": "2026-05-20T17:08:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4586is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4586\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Scott of Florida (for himself and Mr. Cotton ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo require a review of the national security risk posed by communications equipment and services produced or provided by certain entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Blocking CCP Spy Tech Act of 2026 .\n#### 2. Determination of national security risk posed by certain communications equipment and services\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, an appropriate national security agency shall determine if any communications equipment and services described in subsection (b) pose an unacceptable risk to the national security of the United States or the security and safety of United States persons.\n##### (b) Communications equipment and services described\nThe communications equipment or services described in this subsection are any communications equipment or service produced or provided by\u2014\n**(1)**\nGame Science Interactive Co., Ltd.;\n**(2)**\nHangzhou DeepSeek Artificial Intelligence Basic Technology Research Co., Ltd. (commonly known as DeepSeek );\n**(3)**\nHangzhou Yushu Technology Co., Ltd. (commonly known as Unitree Robotics );\n**(4)**\nHangzhou Yunshenchu Technology Co., Ltd. (commonly known as DEEP Robotics );\n**(5)**\nBrainCo, Inc.;\n**(6)**\nManycore Tech, Inc.; or\n**(7)**\nwith respect to an entity described in any of paragraphs (1) through (6) (referred to in this paragraph as a named entity )\u2014\n**(A)**\nany subsidiary, affiliate, or partner of the named entity;\n**(B)**\nany entity in a joint venture with the named entity; or\n**(C)**\nany entity to which the named entity has issued a license to produce or provide that communications equipment or service.\n##### (c) Inclusion of communications services and equipment on covered list\n**(1) Failure to make determination**\nIf an appropriate national security agency does not make a determination as required by subsection (a), the Commission shall, not later than 30 days after the date specified in subsection (a), add all communications equipment and services described in subsection (b) to the covered list.\n**(2) Affirmative determinations**\nNot later than 30 days after an appropriate national security agency determines that any of the communications equipment or services described in subsection (b) present an unacceptable risk to the national security of the United States or the security and safety of United States persons\u2014\n**(A)**\nthe Commission shall place such communications equipment or services on the covered list; and\n**(B)**\nthe appropriate national security agency shall submit to the appropriate congressional committees a report on the determination.\n**(3) Negative determinations**\nNot later than 30 days after an appropriate national security agency determines that any of the communications equipment or services described in subsection (b) do not present an unacceptable risk to the national security of the United States or the security and safety of United States persons\u2014\n**(A)**\nthat agency shall submit to the appropriate congressional committees a report on the determination; and\n**(B)**\nnot later than 180 days following the determination, all other appropriate national security agencies shall review the determination and shall submit to the appropriate congressional committees a report on their determinations.\n**(4) Form**\nEach determination required by this subsection shall be submitted to the appropriate congressional committees in unclassified form, but may include a classified annex.\n##### (d) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services, the Committee on Homeland Security and Governmental Affairs, the Committee on Commerce, Science, and Transportation, and the Select Committee on Intelligence in the Senate; and\n**(B)**\nthe Committee on Armed Services, the Committee on Homeland Security, the Committee on Energy and Commerce, and the Permanent Select Committee on Intelligence in the House of Representatives.\n**(2) Appropriate national security agency**\nThe term appropriate national security agency has the meaning given that term in section 9 of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1608 ).\n**(3) Commission**\nThe term Commission means the Federal Communications Commission.\n**(4) Covered list**\nThe term covered list means the list of covered communications equipment or services published by the Commission under section 2(a) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1601(a) ).\n#### 3. Determination of identification of entities as Chinese military companies\nPursuant to the annual review required under section 1260H(a) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note), the Secretary of Defense shall determine if any entity described in section 2(b) should be identified under such section 1260H(a) as a Chinese military company operating directly or indirectly in the United States.",
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4586is.xml"
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
      "title": "Blocking CCP Spy Tech Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Blocking CCP Spy Tech Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a review of the national security risk posed by communications equipment and services produced or provided by certain entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:18:34Z"
    }
  ]
}
```
