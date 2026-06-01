# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3086?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3086
- Title: Restoring Integrity in Fiduciary Duty Act
- Congress: 119
- Bill type: S
- Bill number: 3086
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2026-04-21T17:45:33Z
- Update date including text: 2026-04-21T17:45:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3086",
    "number": "3086",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Restoring Integrity in Fiduciary Duty Act",
    "type": "S",
    "updateDate": "2026-04-21T17:45:33Z",
    "updateDateIncludingText": "2026-04-21T17:45:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T18:01:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3086is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3086\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Cassidy (for himself and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to clarify the criteria by which a fiduciary may evaluate and select investments based on nonpecuniary factors, and to clarify the application of prudence and exclusive purpose duties to the exercise of shareholder rights.\n#### 1. Short title\nThis Act may be cited as the Restoring Integrity in Fiduciary Duty Act .\n#### 2. Exercise of fiduciary duty in evaluating and selecting investments\n##### (a) In general\nSection 404(a) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104(a) ), is amended by adding at the end the following:\n(3) Investments based on pecuniary factors (A) In general For the purposes of paragraph (1), a fiduciary\u2014 (i) may evaluate an investment or investment course of action based only on pecuniary factors, except as provided in subparagraph (B); (ii) may not subordinate the interests of the participants and beneficiaries in their retirement income or financial benefits under the plan to other objectives; (iii) may not sacrifice investment return or take on additional investment risk to promote nonpecuniary benefits or goals; and (iv) shall weight each pecuniary factor in a manner that appropriately reflects a prudent assessment of the impact of the factor on risk and return. (B) Use of nonpecuniary factors for investment alternatives Notwithstanding subparagraph (A), when choosing between or among investment alternatives, if a fiduciary is unable to distinguish between or among investment alternatives or investment courses of action on the basis of pecuniary factors alone, the fiduciary shall use the capita aut navia standard as the deciding factor in the investment decision, provided that\u2014 (i) the fiduciary documents detail\u2014 (I) why pecuniary factors were not sufficient to select the investment or investment course of action; (II) how the selected investment compares to the alternative investments with regard to the composition of the portfolio with regard to diversification, the liquidity, current return of the portfolio relative to the anticipated cash flow requirements of the plan, and the projected return of the portfolio relative to the funding objectives of the plan; and (III) how the selected investment is consistent with the interests of the participants and beneficiaries in their retirement income or financial benefits under the plan; and (ii) the fiduciary demonstrates that it did not expend any resources during the investment course of action on nonpecuniary factors that place weight between or among investment alternatives for the purpose of the investment decision. (C) Investment alternatives for participant-directed individual account plans In selecting or retaining investment options for a pension plan described in subsection (c)(1)(A), a fiduciary may consider, select, or retain an investment option on the basis that such investment option promotes, seeks, or supports 1 or more nonpecuniary benefits or goals, only if\u2014 (i) the fiduciary satisfies the requirements of paragraph (1) and subparagraphs (A) and (B) of this paragraph in selecting or retaining any such investment option; and (ii) such investment option is not added or retained as, or included as a component of, a default investment described in subsection (c)(5) (or any other default investment alternative). (D) Definitions For the purposes of this paragraph: (i) Capita aut navia The term capita aut navia means a standard by which a fiduciary chooses at random between or among investment alternatives where pecuniary factors are equal and does not give added weight to 1 investment or another, provided that the investment alternatives have identical risk and return attributes and choosing among the investment alternatives would have comparatively negligible impact, not considering liquidity constraints or transaction costs. (ii) Investment course of action The term investment course of action means any series or program of investments or actions related to a fiduciary\u2019s performance of the fiduciary\u2019s investment duties, and includes the selection of an investment fund as a plan investment, or in the case of a plan described in subsection (c)(1)(A), a designated investment alternative under the plan. (iii) Material The term material, when used to qualify a financial risk or financial return\u2014 (I) means a financial risk or financial return in which there is a substantial likelihood that a reasonable investor would attach importance when\u2014 (aa) evaluating the potential financial risks or returns of an existing or prospective investment; or (bb) exercising, or declining to exercise, any rights with respect to securities; and (II) does not include furthering nonpecuniary, environmental, social, political, ideological, or other goals or objectives. (iv) Pecuniary factor The term pecuniary factor means a factor that a fiduciary prudently determines is expected to have a material effect on the risk or return of an investment based on appropriate investment horizons consistent with the plan\u2019s investment objectives and the funding policy established pursuant to section 402(b)(1). .\n##### (b) Effective date\nThe amendments made by this section shall apply to actions taken by a fiduciary on or after the date that is 1 year after the date of enactment of this Act.\n#### 3. Exercise of shareholder rights\n##### (a) In general\nSection 404 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104 ) is amended by adding at the end the following new subsection:\n(f) Exercise of shareholder rights (1) Authority to exercise shareholder rights (A) In general The fiduciary duty to manage plan assets that are shares of stock includes the management of shareholder rights appurtenant to those shares, including the right to vote proxies. When deciding whether to exercise a shareholder right and in exercising such right, including the voting of proxies, a fiduciary shall act prudently and solely in the interests of participants and beneficiaries and for the exclusive purpose of providing benefits to participants and beneficiaries and defraying the reasonable expenses of administering the plan. The fiduciary duty to manage shareholder rights appurtenant to shares of stock does not require the voting of every proxy or the exercise of every shareholder right. (B) Exception This subsection shall not apply to voting, tender, and similar rights with respect to securities that are passed through pursuant to the terms of an individual account plan to participants and beneficiaries with accounts holding such securities. (2) Requirements for exercise of shareholder rights A fiduciary, when deciding whether to exercise a shareholder right and when exercising a shareholder right\u2014 (A) shall\u2014 (i) act solely in accordance with the economic interest of the plan and its participants and beneficiaries; (ii) consider any costs involved; (iii) evaluate material facts that form the basis for any particular proxy vote or exercise of shareholder rights; and (iv) maintain a record of any proxy vote, proxy voting activity, or other exercise of a shareholder right, including any attempt to influence management; and (B) shall not subordinate the interests of participants and beneficiaries in their retirement income or financial benefits under the plan to any nonpecuniary objective, or promote nonpecuniary benefits or goals unrelated to those financial interests of the plan\u2019s participants and beneficiaries. (3) Monitoring A fiduciary shall exercise prudence and diligence in the selection and monitoring of a person, if any, selected to advise or otherwise assist with the exercise of shareholder rights, including by providing research and analysis, recommendations on exercise of proxy voting or other shareholder rights, administrative services with respect to voting proxies, and recordkeeping and reporting services. (4) Investment managers and proxy advisory firms Where the authority to vote proxies or exercise other shareholder rights has been delegated to an investment manager pursuant to section 403(a), or a proxy voting advisory firm or other person who performs advisory services as to the voting of proxies or the exercise of other shareholder rights, a responsible plan fiduciary shall prudently monitor the proxy voting activities of such investment manager or advisory firm and determine whether such activities are in compliance with paragraphs (1) and (2). (5) Voting policies (A) In general In deciding whether to vote a proxy pursuant to this subsection, the plan fiduciary may adopt a proxy voting policy, including a safe harbor proxy voting policy described in subparagraph (B), providing that the authority to vote a proxy shall be exercised pursuant to specific parameters designed to serve the economic interest of the plan. (B) Safe harbor voting policy With respect to a decision not to vote a proxy, a fiduciary shall satisfy the fiduciary responsibilities under this subsection if such fiduciary adopts and is following a safe harbor proxy voting policy that\u2014 (i) limits voting resources to particular types of proposals that the fiduciary has prudently determined are substantially related to the business activities of the issuer or are expected to have a material effect on the value of the plan investment; or (ii) establishes that the fiduciary will refrain from voting on proposals or particular types of proposals when the assets of a plan invested in the issuer relative to the total assets of such plan are below 5 percent (or, in the event such assets are under management, when the assets under management invested in the issuer are below 5 percent of the total assets under management). (C) Exception No proxy voting policy adopted pursuant to this paragraph shall preclude a fiduciary from submitting a proxy vote when the fiduciary determines that the matter being voted on is expected to have a material economic effect on the investment performance of a plan\u2019s portfolio (or the investment performance of assets under management in the case of an investment manager); provided, however, that in all cases compliance with a safe harbor voting policy shall be presumed to satisfy fiduciary responsibilities with respect to decisions not to vote. (6) Review A fiduciary shall periodically review any policy adopted under this subsection. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to an exercise of shareholder rights occurring on or after January 1, 2026.",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-03-10",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1996",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Retirement Proxy Protection Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-11-25T20:33:31Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3086is.xml"
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
      "title": "Restoring Integrity in Fiduciary Duty Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Integrity in Fiduciary Duty Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to clarify the criteria by which a fiduciary may evaluate and select investments based on nonpecuniary factors, and to clarify the application of prudence and exclusive purpose duties to the exercise of shareholder rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:17Z"
    }
  ]
}
```
