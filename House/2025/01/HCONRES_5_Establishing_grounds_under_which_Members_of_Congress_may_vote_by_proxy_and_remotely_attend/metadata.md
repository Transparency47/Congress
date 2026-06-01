# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/5?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/5
- Title: Legislative Proxy and Absence Accommodation Resolution
- Congress: 119
- Bill type: HCONRES
- Bill number: 5
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-03-07T21:12:50Z
- Update date including text: 2025-03-07T21:12:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/5",
    "number": "5",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Legislative Proxy and Absence Accommodation Resolution",
    "type": "HCONRES",
    "updateDate": "2025-03-07T21:12:50Z",
    "updateDateIncludingText": "2025-03-07T21:12:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-28T16:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres5ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 5\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Williams of Georgia submitted the following concurrent resolution; which was referred to the Committee on Rules\nCONCURRENT RESOLUTION\nEstablishing grounds under which Members of Congress may vote by proxy and remotely attend committee proceedings in the event of illness, a death in the family, jury service, military service, and other emergency situations, and for other purposes.\n#### 1. Short title\nThis resolution may be cited as the Legislative Proxy and Absence Accommodation Resolution .\n#### 2. Permitting proxy voting and remote attendance at committee proceedings for Members of the House of Representatives in certain cases\n##### (a) Proxy voting\nRule III of the Rules of the House of Representatives is amended\u2014\n**(1)**\nin clause 2(a), by striking A Member may not and inserting Except as provided in clause 4, a Member may not ;\n**(2)**\nin clause 2(b), by striking No other person may and inserting Except as provided in clause 4, no other person may ; and\n**(3)**\nby adding at the end the following new clause:\nProxy voting 4. (a) If any of the grounds described in paragraph (b) applies to a Member, such Member may designate another Member as a proxy who may cast the vote of such Member or record the presence of such Member in the House if such Member submits to the Clerk a signed letter (which may be in electronic form)\u2014 (1) certifying that one of those grounds applies to such Member; and (2) specifying by name the other Member who is designated as a proxy for such Member. (b) The grounds described in this paragraph with respect to a Member are as follows: (1) Any of the grounds under which an eligible employee is entitled to leave under subparagraphs (A) through (E) of section 102(a)(1) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a)(1) ), but only if the Member includes with the signed letter required under this paragraph such documentation as the Clerk may require. (2) An illness of the Member which would not be treated as a serious health condition under section 102(a)(1)(D) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a)(1)(D) ) if the Member were an eligible employee under such Act, except that the number of days during which a Member may designate a proxy under this clause on the basis of this subparagraph in a calendar year may not exceed 7. (3) The summoning of the Member, in connection with a judicial proceeding, by a court or authority responsible for the conduct of that proceeding, to serve as a juror, but only if the Member includes with the signed letter required under this paragraph such documentation of the summoning as the Clerk may require. (4) The death of a family member, except that the number of consecutive days during which a Member may designate a proxy under this clause on the basis of this subparagraph with respect to a family member may not exceed 4. For purposes of this subparagraph, the term family member means a spouse (including a domestic partner) and a spouse\u2019s parent; a child and a child\u2019s spouse; a parent and a parent\u2019s spouse; a sibling and a sibling\u2019s spouse; a grandparent, a grandchild, or a spouse of a grandparent or grandchild; and any other individual who is related by blood or affinity and whose association with the individual is the equivalent of a family relationship under regulations issued by the Committee on House Administration. (5) The Member is absent by reason of service in the uniformed services, as defined in section 4303(13) of title 38, United States Code, except that the number of days during which a Member may designate a proxy under this clause on the basis of this subparagraph in a calendar year may not exceed 15 in the case of service consisting of active duty, active duty for training, and inactive duty training and may not exceed 22 days in the case of service consisting of State active duty in response to a national emergency or a major disaster referred to in such section. A Member may designate a proxy under this clause on the basis of this subparagraph only if the Member includes with the signed letter required under this paragraph such documentation of the service as the Clerk may require. (6) The Member is prevented from safely traveling to or performing work at the location of the committee proceeding due to\u2014 (A) an act of God; (B) a terrorist attack; or (C) another condition that prevents the Member from safely traveling to or performing work at the location of the proceeding. (c) The Clerk shall maintain an updated list of the following information, and shall make such list publicly available in electronic form: (1) The designations submitted or in effect under paragraph (a). (2) With respect to each Member who designated a proxy under paragraph (a)\u2014 (A) the number of days for which the Member designated a proxy; and (B) the grounds under paragraph (b) on which the Member designated the proxy. (d) Any Member whose vote is cast or whose presence is recorded by a designated proxy under this clause shall be counted for the purpose of establishing a quorum under the rules of the House. .\n##### (b) Remote attendance at committee proceedings\nRule XI of the Rules of the House of Representatives is amended by adding at the end the following new clause:\nRemote attendance at committee proceedings in certain cases 7. (a) Notwithstanding any other provision of this rule, if any of the grounds described in paragraph (b) applies to a Member and such Member has submitted to the Clerk a signed letter (which may be in electronic form) certifying that one of those grounds applies to such Member\u2014 (1) such Member may participate remotely during in-person committee proceedings, including by casting a vote or recording such Member\u2019s presence remotely; (2) such remote participation shall not be considered an absence for purposes of clause 5(c) of rule X or clause 2(d) of rule XI; and (3) such Member shall be counted for the purpose of establishing a quorum under the rules of the House and the committee. (b) The grounds described in this paragraph with respect to a Member are as follows: (1) Any of the grounds under which an eligible employee is entitled to leave under subparagraphs (A) through (E) of section 102(a)(1) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a)(1) ), but only if the Member includes with the signed letter required under this paragraph such documentation as the Clerk may require. (2) An illness of the Member which would not be treated as a serious health condition under section 102(a)(1)(D) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a)(1)(D) ) if the Member were an eligible employee under such Act, except that the number of days during which a Member may participate remotely under this clause on the basis of this subparagraph in a calendar year may not exceed 7. (3) The summoning of the Member, in connection with a judicial proceeding, by a court or authority responsible for the conduct of that proceeding, to serve as a juror, but only if the Member includes with the signed letter required under this paragraph such documentation of the summoning as the Clerk may require. (4) The death of a family member, except that the number of consecutive days during which a Member may participate remotely under this clause on the basis of this subparagraph with respect to a family member may not exceed 4. For purposes of this subparagraph, the term family member means a spouse (including a domestic partner) and a spouse\u2019s parent; a child and a child\u2019s spouse; a parent and a parent\u2019s spouse; a sibling and a sibling\u2019s spouse; a grandparent, a grandchild, or a spouse of a grandparent or grandchild; and any other individual who is related by blood or affinity and whose association with the individual is the equivalent of a family relationship under regulations issued by the Committee on House Administration. (5) The Member is absent by reason of service in the uniformed services, as defined in section 4303(13) of title 38, United States Code, except that the number of days during which a Member may participate remotely under this clause on the basis of this subparagraph in a calendar year may not exceed 15 in the case of service consisting of active duty, active duty for training, and inactive duty training and may not exceed 22 days in the case of service consisting of State active duty in response to a national emergency or a major disaster referred to in such section. A Member may participate remotely under this clause on the basis of this subparagraph only if the Member includes with the signed letter required under this paragraph such documentation of the service as the Clerk may require. (6) The Member is prevented from safely traveling to or performing work at the location of the committee proceeding due to\u2014 (A) an act of God; (B) a terrorist attack; or (C) another condition that prevents the Member from safely traveling to or performing work at the location of the proceeding. (c) The Clerk shall maintain an updated list of the following information, and shall make such list publicly available in electronic form: (1) The Members who are eligible to participate remotely under this clause. (2) With respect to each such Member\u2014 (A) the number of days for which the Member participated remotely; and (B) the grounds under paragraph (b) on which the Member participated remotely. .\n#### 3. Permitting proxy voting and remote attendance at committee proceedings for Senators in certain cases\n##### (a) Proxy voting\n**(1) Authorizing designation of proxies**\nNotwithstanding any other provision of any of the Standing Rules of the Senate, if any of the grounds described in subsection (c) applies to a Senator, such Senator may designate another Senator as a proxy who may cast the vote of such Senator or record the presence of such Senator in the Senate if such Senator submits to the Secretary of the Senate a signed letter (which may be in electronic form)\u2014\n**(A)**\ncertifying that one of those grounds applies to such Senator; and\n**(B)**\nspecifying by name the other Senator who is designated as a proxy for such Senator.\n**(2) Determination of quorum**\nAny Senator whose vote is cast or whose presence is recorded by a designated proxy under this section shall be counted for the purpose of establishing a quorum under the Standing Rules of the Senate.\n##### (b) Remote attendance at committee proceedings\nNotwithstanding any other provision of any of the Standing Rules of the Senate, if any of the grounds described in subsection (c) applies to a Senator, and such Senator has submitted to the Secretary of the Senate a signed letter (which may be in electronic form) certifying that one of those grounds applies to such Senator, such Senator may participate remotely during in-person committee proceedings, including by casting a vote or recording such Senator\u2019s presence remotely, and\u2014\n**(1)**\nsuch remote participation shall not be considered an absence for purposes of any provision of the Standing Rules of the Senate; and\n**(2)**\na Senator participating remotely pursuant to this subsection shall be counted for the purpose of establishing a quorum under the Standing Rules of the Senate and the committee.\n##### (c) Grounds described\nThe grounds described in this subsection with respect to a Senator are as follows:\n**(1)**\nAny of the grounds under which an eligible employee is entitled to leave under subparagraphs (A) through (E) of section 102(a)(1) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a)(1) ), but only if the Member includes with the signed letter required under this paragraph such documentation as the Secretary may require.\n**(2)**\nAn illness of the Senator which would not be treated as a serious health condition under section 102(a)(1)(D) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a)(1)(D) ) if the Senator were an eligible employee under such Act, except that the number of days during which a Senator may designate a proxy under subsection (a) or may participate remotely under subsection (b) on the basis of this paragraph in a calendar year may not exceed 7.\n**(3)**\nThe summoning of the Senator, in connection with a judicial proceeding, by a court or authority responsible for the conduct of that proceeding, to serve as a juror, but only if the Senator includes with the signed letter required under this paragraph such documentation of the summoning as the Clerk may require.\n**(4)**\nThe death of a family member, except that the number of consecutive days during which a Senator may designate a proxy under subsection (a) or may participate remotely under subsection (b) on the basis of this paragraph with respect to a family member may not exceed 4. For purposes of this paragraph, the term family member means a spouse (including a domestic partner) and a spouse\u2019s parent; a child and a child\u2019s spouse; a parent and a parent\u2019s spouse; a sibling and a sibling\u2019s spouse; a grandparent, a grandchild, or a spouse of a grandparent or grandchild; and any other individual who is related by blood or affinity and whose association with the individual is the equivalent of a family relationship under regulations issued by the Committee on Rules and Administration.\n**(5)**\nThe Senator is absent by reason of service in the uniformed services, as defined in section 4303(13) of title 38, United States Code, except that the number of days during which a Senator may designate a proxy under subsection (a) or may participate remotely under subsection (b) on the basis of this paragraph in a calendar year may not exceed 15 in the case of service consisting of active duty, active duty for training, and inactive duty training and may not exceed 22 days in the case of service consisting of State active duty in response to a national emergency or a major disaster referred to in such section. A Senator may designate a proxy under subsection (a) or may participate remotely under subsection (b) on the basis of this paragraph only if the Senator includes with the signed letter required under such subsections such documentation of the service as the Secretary may require.\n**(6)**\nThe Senator is prevented from safely traveling to or performing work at the location of the committee proceeding due to\u2014\n**(A)**\nan act of God;\n**(B)**\na terrorist attack; or\n**(C)**\nanother condition that prevents the Senator from safely traveling to or performing work at the location of the proceeding.\n##### (d) Maintenance of information by Secretary\nThe Secretary shall maintain an updated list of the following information, and shall make such list publicly available in electronic form:\n**(1)**\nThe designations of proxies submitted or in effect under subsection (a).\n**(2)**\nWith respect to each Senator who designated a proxy under subsection (a)\u2014\n**(A)**\nthe number of days for which the Senator designated a proxy; and\n**(B)**\nthe grounds under subsection (c) on which the Senator designated the proxy.\n**(3)**\nThe Senators who are eligible to participate remotely under subsection (b).\n**(4)**\nWith respect to each Senator who is eligible to participate remotely under subsection (b)\u2014\n**(A)**\nthe number of days for which the Senator participated remotely; and\n**(B)**\nthe grounds under subsection (c) on which the Senator participated remotely.",
      "versionDate": "2025-01-28",
      "versionType": "IH"
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
            "name": "Congressional committees",
            "updateDate": "2025-02-28T15:18:16Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-02-28T15:18:10Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-28T15:18:03Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-28T15:17:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-31T14:25:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "House",
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
          "measure-id": "id119hconres5",
          "measure-number": "5",
          "measure-type": "hconres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres5v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Legislative Proxy and Absence Accommodation Resolution</strong></p><p>This concurrent resolution authorizes proxy voting and remote appearances by Members of\u00a0Congress\u00a0who are\u00a0absent due to an\u00a0illness, military service,\u00a0jury duty, or other circumstances.\u00a0</p><p>The concurrent resolution establishes grounds and procedures by which an absent Member of the House of Representatives or the Senate may (1) designate another Member to cast a vote or record the presence of the absent Member; and (2) remotely appear at a committee proceeding.</p><p>The concurrent resolution authorizes proxy voting and remote appearances for absences due to</p><ul><li>jury duty;</li><li>the death of a family member;</li><li>a family member who has a serious health condition;</li><li>the Member's own\u00a0illness or serious health condition; </li><li>the birth, adoption, or foster placement of a son or daughter;</li><li>the Member serving in the armed services;</li><li>a family member being called to active duty;\u00a0or</li><li>a condition preventing the Member from safely traveling to or performing work at the proceeding.</li></ul><p>Certain purposes are time-limited; for example, an absence due to a Member's own illness is limited to seven days in a calendar year.</p><p>Further, a Member must provide to the Clerk of the House or the Secretary of the Senate, respectively\u00a0(1) a written proxy designation or notice of remote appearance, (2) the grounds for the absence, and (3) such documentation as they may require.\u00a0The Clerk and Secretary must maintain and make publicly available a list of the grounds, time frames, and other details about Members\u00a0using these provisions.</p>"
        },
        "title": "Legislative Proxy and Absence Accommodation Resolution"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres5.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Legislative Proxy and Absence Accommodation Resolution</strong></p><p>This concurrent resolution authorizes proxy voting and remote appearances by Members of\u00a0Congress\u00a0who are\u00a0absent due to an\u00a0illness, military service,\u00a0jury duty, or other circumstances.\u00a0</p><p>The concurrent resolution establishes grounds and procedures by which an absent Member of the House of Representatives or the Senate may (1) designate another Member to cast a vote or record the presence of the absent Member; and (2) remotely appear at a committee proceeding.</p><p>The concurrent resolution authorizes proxy voting and remote appearances for absences due to</p><ul><li>jury duty;</li><li>the death of a family member;</li><li>a family member who has a serious health condition;</li><li>the Member's own\u00a0illness or serious health condition; </li><li>the birth, adoption, or foster placement of a son or daughter;</li><li>the Member serving in the armed services;</li><li>a family member being called to active duty;\u00a0or</li><li>a condition preventing the Member from safely traveling to or performing work at the proceeding.</li></ul><p>Certain purposes are time-limited; for example, an absence due to a Member's own illness is limited to seven days in a calendar year.</p><p>Further, a Member must provide to the Clerk of the House or the Secretary of the Senate, respectively\u00a0(1) a written proxy designation or notice of remote appearance, (2) the grounds for the absence, and (3) such documentation as they may require.\u00a0The Clerk and Secretary must maintain and make publicly available a list of the grounds, time frames, and other details about Members\u00a0using these provisions.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hconres5"
    },
    "title": "Legislative Proxy and Absence Accommodation Resolution"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Legislative Proxy and Absence Accommodation Resolution</strong></p><p>This concurrent resolution authorizes proxy voting and remote appearances by Members of\u00a0Congress\u00a0who are\u00a0absent due to an\u00a0illness, military service,\u00a0jury duty, or other circumstances.\u00a0</p><p>The concurrent resolution establishes grounds and procedures by which an absent Member of the House of Representatives or the Senate may (1) designate another Member to cast a vote or record the presence of the absent Member; and (2) remotely appear at a committee proceeding.</p><p>The concurrent resolution authorizes proxy voting and remote appearances for absences due to</p><ul><li>jury duty;</li><li>the death of a family member;</li><li>a family member who has a serious health condition;</li><li>the Member's own\u00a0illness or serious health condition; </li><li>the birth, adoption, or foster placement of a son or daughter;</li><li>the Member serving in the armed services;</li><li>a family member being called to active duty;\u00a0or</li><li>a condition preventing the Member from safely traveling to or performing work at the proceeding.</li></ul><p>Certain purposes are time-limited; for example, an absence due to a Member's own illness is limited to seven days in a calendar year.</p><p>Further, a Member must provide to the Clerk of the House or the Secretary of the Senate, respectively\u00a0(1) a written proxy designation or notice of remote appearance, (2) the grounds for the absence, and (3) such documentation as they may require.\u00a0The Clerk and Secretary must maintain and make publicly available a list of the grounds, time frames, and other details about Members\u00a0using these provisions.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hconres5"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres5ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Legislative Proxy and Absence Accommodation Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Legislative Proxy and Absence Accommodation Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-29T11:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Establishing grounds under which Members of Congress may vote by proxy and remotely attend committee proceedings in the event of illness, a death in the family, jury service, military service, and other emergency situations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:18Z"
    }
  ]
}
```
