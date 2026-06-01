# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/369
- Title: NO GOTION Act
- Congress: 119
- Bill type: S
- Bill number: 369
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2026-05-15T12:45:14Z
- Update date including text: 2026-05-15T12:45:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/369",
    "number": "369",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
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
    "title": "NO GOTION Act",
    "type": "S",
    "updateDate": "2026-05-15T12:45:14Z",
    "updateDateIncludingText": "2026-05-15T12:45:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T22:37:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s369is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 369\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny certain green energy tax benefits to companies associated with foreign adversaries.\n#### 1. Short title\nThis Act may be cited as the No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act .\n#### 2. Denial of green energy tax benefits to companies associated with foreign adversaries\n##### (a) In general\nChapter 77 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n7531. Denial of green energy tax benefits to companies associated with foreign adversaries (a) In general In the case of any disqualified company, this title shall be applied without regard to sections 30C, 40, 40A, 40B, 45, 45Q, 45U, 45V, 45W, 45X, 45Y, 45Z, 48, 48C, 48E, 179D, 6426(c), 6426(d), 6426(e), and 6427(e). (b) Disqualified company (1) In general (A) Definition For purposes of this section, the term disqualified company means any entity described in subparagraphs (B) through (D). (B) Foreign adversary parties The entities described in this subparagraph consist of the following: (i) The government of a foreign adversary, any agency or government instrumentality of a foreign adversary, or any entity which is directly or indirectly owned, controlled, or directed by any such government, agency, or government instrumentality. (ii) Any entity organized under the laws of a foreign adversary (or any political subdivision thereof) or whose headquarters is located within a foreign adversary. (C) Owned, controlled, directed, or influenced by foreign adversary parties The entities described in this subparagraph consist of the following: (i) Any entity for which, on any date during the taxable year, not less than 10 percent of the outstanding equity interests (by value, voting, governance, board appointment, or similar rights or influence) are held directly or indirectly by, or on behalf of, 1 or more of the entities described in subparagraph (B), including through interests in co-investment vehicles, joint ventures, or similar arrangements. (ii) Any entity which is directly or indirectly controlled, directed, or materially influenced by any entity described in subparagraph (B). (iii) Any entity for which the actions, management, ownership, or operations of such entity are subject to the direct influence of an entity described in subparagraph (B). (iv) Any entity for which an interest in such entity is held by an entity described in subparagraph (B) (referred to in this clause as the beneficiary firm ) as a derivative financial instrument or through a contractual arrangement between the beneficiary firm and such entity, including any financial instrument or other contract between the beneficiary firm and the entity which seeks to replicate any financial return with respect to such entity or interest in such entity. (D) Debt or other arrangements with foreign adversary parties (i) In general An entity is described in this subparagraph if, as a result of any prohibited obligation or arrangement\u2014 (I) the actions, management, or operations of such entity are subject to the direct or indirect influence of 1 or more entities described in subparagraph (B) or (C), or (II) such entity provides a substantial benefit to 1 or more entities described in subparagraph (B) or (C). (ii) Prohibited obligation or arrangement For purposes of this subparagraph, the term prohibited obligation or arrangement means any\u2014 (I) debt, (II) lease or sublease arrangement, (III) management or operating arrangement, (IV) contract manufacturing arrangement, (V) license or sublicense agreement, or (VI) financial derivative. (iii) Exception (I) In general For purposes of clause (i)(II), the purchase of equipment or manufacturing inputs in an arm's length transaction shall not, in and of itself, be deemed to provide a substantial benefit. (II) Arm's length For purposes of this clause, the term arm's length has the meaning given in section 1.482\u20131 of title 26, Code of Federal Regulations. (E) Other definitions For purposes of this paragraph\u2014 (i) Control The term control has the meaning given in section 800.208 of title 31, Code of Federal Regulations (as in effect on the date of enactment of the No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act ). (ii) Foreign adversary The term foreign adversary has the meaning given the term covered nation in section 4872(d)(2) of title 10, United States Code, except that such term shall also include\u2014 (I) the Republic of Cuba, and (II) the Boliverian Republic of Venezuela during any period of time during which Nicholas Maduro is President of the Republic. (2) Administration The Secretary may issue such guidance as is necessary to carry out the purposes of this section, including establishment of rules for\u2014 (A) implementation of paragraph (1)(C)(i) for determination of whether the percentage requirements with respect to outstanding equity interests have been satisfied in the case of an entity for which the stock of such entity is traded on an established securities market in the United States or any foreign country, and (B) preventing entities from evading, circumventing, or abusing the application of the requirements under this section. .\n##### (b) Clerical amendment\nThe table of sections for chapter 77 of such Code is amended by adding at the end the following new item:\nSec. 7531. Denial of green energy tax benefits to companies associated with foreign adversaries. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-03",
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
        "name": "Taxation",
        "updateDate": "2025-04-29T15:22:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-03",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s369",
          "measure-number": "369",
          "measure-type": "s",
          "orig-publish-date": "2025-02-03",
          "originChamber": "SENATE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s369v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2025-02-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act</strong></p><p>This bill prohibits certain entities associated with China, Cuba, Iran, North Korea, Russia, or the Maduro regime of Venezuela from claiming various energy-related federal tax incentives.</p><p>Specifically,\u00a0certain energy-related federal tax incentives may not be claimed by</p><ul><li>the government, a government instrumentality, or an agency of China, Cuba, Iran, North Korea, Russia, or\u00a0the regime of Nicolas\u00a0Maduro in Venezuela;</li><li>any entity that is organized under the laws of or is headquartered in one of these countries; or</li><li>any entity that is owned, controlled, directed, or influenced by\u00a0or that has certain financial or contractual connections with any such government, government instrumentality, agency, or entity.</li></ul><p>Such entities may not claim the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, and</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>"
        },
        "title": "NO GOTION Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s369.xml",
    "summary": {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act</strong></p><p>This bill prohibits certain entities associated with China, Cuba, Iran, North Korea, Russia, or the Maduro regime of Venezuela from claiming various energy-related federal tax incentives.</p><p>Specifically,\u00a0certain energy-related federal tax incentives may not be claimed by</p><ul><li>the government, a government instrumentality, or an agency of China, Cuba, Iran, North Korea, Russia, or\u00a0the regime of Nicolas\u00a0Maduro in Venezuela;</li><li>any entity that is organized under the laws of or is headquartered in one of these countries; or</li><li>any entity that is owned, controlled, directed, or influenced by\u00a0or that has certain financial or contractual connections with any such government, government instrumentality, agency, or entity.</li></ul><p>Such entities may not claim the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, and</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119s369"
    },
    "title": "NO GOTION Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act or the NO GOTION Act</strong></p><p>This bill prohibits certain entities associated with China, Cuba, Iran, North Korea, Russia, or the Maduro regime of Venezuela from claiming various energy-related federal tax incentives.</p><p>Specifically,\u00a0certain energy-related federal tax incentives may not be claimed by</p><ul><li>the government, a government instrumentality, or an agency of China, Cuba, Iran, North Korea, Russia, or\u00a0the regime of Nicolas\u00a0Maduro in Venezuela;</li><li>any entity that is organized under the laws of or is headquartered in one of these countries; or</li><li>any entity that is owned, controlled, directed, or influenced by\u00a0or that has certain financial or contractual connections with any such government, government instrumentality, agency, or entity.</li></ul><p>Such entities may not claim the federal tax credits for</p><ul><li>alternative fuel vehicle refueling property,</li><li>second-generation\u00a0biofuel,</li><li>biodiesel fuel,</li><li>sustainable aviation fuel,</li><li>renewable electricity production,</li><li>carbon sequestration,</li><li>zero-emission nuclear power production,</li><li>clean hydrogen production,</li><li>clean commercial vehicles,</li><li>advanced manufacturing production,</li><li>clean electricity production,</li><li>clean fuel production,</li><li>investments in energy property,</li><li>advanced energy projects,</li><li>clean electricity investment,</li><li>biodiesel mixtures,</li><li>alternative fuel, and</li><li>alternative fuel mixtures.</li></ul><p>Further, such entities are prohibited from claiming the federal tax deduction for energy efficient improvements to commercial buildings.</p><p>Finally, such entities are not entitled to a credit or refund of federal excise taxes paid\u00a0on biodiesel, alternative fuel, or sustainable aviation fuel mixtures produced by the entities.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119s369"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s369is.xml"
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
      "title": "NO GOTION Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NO GOTION Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Official Giveaways Of Taxpayers\u2019 Income to Oppressive Nations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to deny certain green energy tax benefits to companies associated with foreign adversaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:33Z"
    }
  ]
}
```
