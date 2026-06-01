# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/384
- Title: One Agency Act
- Congress: 119
- Bill type: HR
- Bill number: 384
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2025-10-09T03:26:16Z
- Update date including text: 2025-10-09T03:26:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/384",
    "number": "384",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "One Agency Act",
    "type": "HR",
    "updateDate": "2025-10-09T03:26:16Z",
    "updateDateIncludingText": "2025-10-09T03:26:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:02:00Z",
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
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "WI"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "WY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr384ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 384\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Cline (for himself, Mr. Fitzgerald , and Ms. Hageman ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo transfer antitrust enforcement from the Federal Trade Commission to the Attorney General, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Agency Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIt is the policy of the United States to promote the vigorous, effective, and efficient enforcement of the antitrust laws.\n**(2)**\nThe overlapping antitrust enforcement jurisdiction of the Department of Justice and the Federal Trade Commission has wasted taxpayer resources, hampered enforcement efforts, and caused uncertainty for businesses and consumers in the United States.\n**(3)**\nIt is preferable that primary Federal responsibility for enforcing the antitrust laws of the United States be given to a single entity, and the Department of Justice is best suited to do so.\n#### 3. Definitions\nIn this Act:\n**(1) Antitrust laws**\nThe term antitrust laws means\u2014\n**(A)**\nthe Sherman Act ( 15 U.S.C. 1 et seq. ); and\n**(B)**\nthe Clayton Act ( 15 U.S.C. 12 et seq. ).\n**(2) Effective date**\nThe term effective date means the date described in section 6.\n**(3) FTC**\nThe term FTC means the Federal Trade Commission.\n**(4) FTC antitrust action**\nThe term FTC antitrust action means any investigation, litigation, administrative proceeding, or other action at the FTC that\u2014\n**(A)**\nis supervised by an FTC antitrust unit; or\n**(B)**\nrelates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date.\n**(5) FTC antitrust assets**\nThe term FTC antitrust assets \u2014\n**(A)**\nmeans all electronic or tangible records and files relating to matters supervised, as well as any physical assets or equipment owned and used or retained, by an FTC antitrust unit; and\n**(B)**\ndoes not include any office space or leased facilities or equipment.\n**(6) FTC antitrust employee**\nThe term FTC antitrust employee means an individual who on the day before the effective date is employed by the FTC and assigned to an FTC antitrust unit.\n**(7) FTC antitrust funding**\nThe term FTC antitrust funding means all amounts appropriated before the effective date by an Act of Congress to the FTC that are designated, by Congress or the FTC for an FTC antitrust unit.\n**(8) FTC antitrust unit**\nThe term FTC antitrust unit means\u2014\n**(A)**\nthe Bureau of Competition of the FTC; and\n**(B)**\neach division of the Bureau of Economics of the FTC that is designated to work on FTC antitrust actions.\n**(9) Transition period**\nThe term transition period means the period beginning on the effective date and ending on the later of\u2014\n**(A)**\nthe date that is 1 year after the effective date; or\n**(B)**\nthe date that is 180 days after the date described in subparagraph (A), which may be extended by the Attorney General once for an additional 180 days, if the Attorney General determines that a period longer than the period described in subparagraph (A) is necessary to avoid harm to the interests of the United States or the effective enforcement of the antitrust laws.\n#### 4. Transfer of antitrust enforcement functions from the FTC to the Attorney General\n##### (a) Transfer of actions\n**(1) In general**\nThere shall be transferred to the Attorney General all FTC antitrust actions, FTC antitrust employees, FTC antitrust assets, and FTC antitrust funding on the earlier of\u2014\n**(A)**\nthe date determined by the Attorney General under paragraph (2)(B); or\n**(B)**\nthe end of the transition period.\n**(2) Requirement**\nThe Attorney General, taking care to minimize disruption to ongoing enforcement matters and in consultation as necessary with the Office of Personnel Management, the General Services Administration, and the Chairman of the FTC, shall\u2014\n**(A)**\ntake all necessary actions to complete implementation of this Act before the end of the transition period; and\n**(B)**\ndetermine the dates certain, which may not be earlier than the effective date or later than the end of the transition period, on which the transfers under paragraph (1) shall occur.\n**(3) Personnel**\n**(A) Assignment**\nAn FTC antitrust employee transferred to the Attorney General under this Act shall be assigned to the Antitrust Division of the Department of Justice.\n**(B) Office space**\nOn the request of the Attorney General, and in consultation as necessary with the General Services Administration, the FTC shall allow the Attorney General to use any office space or leased facilities previously used by FTC antitrust employees until such time as the Attorney General may provide office space or facilities. After the transfer of FTC antitrust funding to the Attorney General, the Attorney General shall compensate the FTC for the costs of the use of such office space or leased facilities.\n**(C) Restructuring**\nNotwithstanding any other provision of law, the Attorney General is authorized to restructure the Antitrust Division of the Department of Justice before the expiration of the transition period, as the Attorney General determines is appropriate, to carry out the purposes of this Act and accomplish the efficient enforcement of the antitrust laws.\n**(4) Antitrust actions**\n**(A) In general**\nAs soon as is reasonably practicable during the transition period, all open investigations, studies, litigations, matters, or other proceedings being supervised by an FTC antitrust unit and relating to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date, shall be transferred to and assumed by the Attorney General.\n**(B) Handling of administrative actions**\nFTC antitrust actions that were initiated by the FTC and were unresolved as of the first day of the transition period, shall be\u2014\n**(i)**\ncontinued as the Attorney General determines is appropriate; and\n**(ii)**\nthe FTC shall have the power to deputize former FTC antitrust employees, with the consent of the Attorney General, to continue any FTC antitrust actions as described in clause (i).\n**(C) Intervention**\nAny FTC antitrust actions before a court of the United States as of the first day of the transition period, that were initiated by the FTC and were unresolved as of the first day of the transition period, shall be\u2014\n**(i)**\ncontinued as the Attorney General determines is appropriate; and\n**(ii)**\nthat the FTC shall have the power to deputize former FTC antitrust employees, with the consent of the Attorney General, to continue any FTC antitrust actions as described in clause (i).\n**(D) Consent decrees**\n**(i) In general**\nAt the end of the transition period, the Attorney General shall have sole authority to receive all reports as required under, enforce violations of, approve modifications to, or rescind any consent decree entered into by the FTC before the effective date that concerns conduct alleged to violate the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date.\n**(ii) Administrative enforcement**\nIf deemed necessary by the FTC and the Attorney General, the FTC shall have the power to deputize former FTC antitrust employees, with the consent of the Attorney General, to enforce and negotiate modifications of FTC consent decrees in effect on the day before the effective date in the FTC\u2019s administrative process.\n**(5) Authority to conduct investigative studies**\n**(A) Reports of persons, partnerships, and corporations**\n**(i) In general**\nThe Attorney General may require, by general or special orders, persons, partnerships, and corporations, engaged in or whose business affects commerce to file with the Attorney General in such form as the Attorney General may prescribe annual or special reports or answers in writing to specific questions, furnishing to the Attorney General such information as the Attorney General may require as to the organization, business, conduct, practices, management, and relation to other corporations, partnerships, and individuals of the respective persons, partnerships, and corporations filing such reports or answers in writing.\n**(ii) Oath**\nReports and answers required under clause (i) shall\u2014\n**(I)**\nbe made under oath or otherwise as the Attorney General may prescribe;\n**(II)**\npertain solely to competition or the application of the antitrust laws; and\n**(III)**\nbe filed with the Attorney General within such reasonable period as the Attorney General may prescribe, unless additional time be granted in any case by the Attorney General.\n**(B) Publication of information or reports**\n**(i) In general**\nExcept as provided in clause (ii), the Attorney General\u2014\n**(I)**\nshall make public from time to time such portions of the information obtained by the Attorney General under this paragraph as are in the public interest;\n**(II)**\nmay make annual and special reports to Congress that include recommendations for additional legislation; and\n**(III)**\nshall provide for the publication of reports and decisions of the Attorney General in such form and manner as may be best adapted for public information and use.\n**(ii) Prohibition against publication of privileged or confidential information**\n**(I) In general**\nExcept as provided in subclause (II), the Attorney General shall not make public any trade secret or any commercial or financial information that is obtained from any person and that is privileged or confidential.\n**(II) Exception**\nThe Attorney General may disclose information described in subclause (I) to\u2014\n**(aa)**\nofficers and employees of appropriate Federal law enforcement agencies or to any officer or employee of any State law enforcement agency on the prior certification of an officer of any such Federal or State law enforcement agency that such information will be maintained in confidence and will be used only for official law enforcement purposes; or\n**(bb)**\nany officer or employee of any foreign law enforcement agency under the same circumstances that making material available to foreign law enforcement agencies is permitted under section 21(b) of the Federal Trade Commission Act ( 15 U.S.C. 57b\u20132(b) ).\n**(6) Benefit of antitrust division**\nAll FTC antitrust assets and FTC antitrust funding transferred under this subsection shall be for the exclusive use and benefit of the Antitrust Division of the Department of Justice, except to the extent the FTC deputizes former FTC antitrust employees, with the consent of the Attorney General, to continue any FTC antitrust actions that are ongoing and unresolved before the effective date.\n##### (b) Transition period\n**(1) In general**\nExcept as provided in paragraph (2), beginning on the effective date, the FTC may not\u2014\n**(A)**\nhire or assign an employee to an FTC antitrust unit;\n**(B)**\nopen a new investigation or matter within an FTC antitrust unit or relating to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act;\n**(C)**\nwithout the approval of the Attorney General, enter into a consent decree, enter into a settlement agreement, or otherwise resolve an FTC antitrust action; or\n**(D)**\ninitiate a new FTC antitrust action.\n**(2) Enforcement on behalf of the Attorney General**\nNotwithstanding paragraph (1), during the transition period, the Attorney General may deputize an FTC antitrust employee to investigate or prosecute an alleged violation of the antitrust laws on behalf of the Attorney General before the completion of the transfer of personnel under subsection (a).\n**(3) Same rights and obligations**\n**(A) In general**\nNotwithstanding any other provision of law, during the transition period all Department of Justice employees under the supervision of the Attorney General shall have the same rights and obligations with respect to confidential information submitted to the FTC as FTC antitrust employees on the day before the effective date.\n**(B) Rule of construction**\nNothing in this paragraph may be construed as implying any change to the rights and obligations described in subparagraph (A) as a result of this Act.\n##### (c) Agreements\nThe Attorney General, in consultation with the Chairman of the FTC, shall\u2014\n**(1)**\nreview any agreements between the FTC and any other Federal agency or any foreign law enforcement agency; and\n**(2)**\nbefore the end of the transition period, seek to amend, transfer, or rescind such agreements as necessary and appropriate to carry out this Act, endeavoring to complete such amendment, transfer, or rescindment with all due haste.\n##### (d) Rules\nThe Attorney General shall, pursuant to section 7A of the Clayton Act ( 15 U.S.C. 18a ) and in accordance with section 553 of title 5, United States Code, prescribe or amend any rules as necessary to carry out the Clayton Act.\n#### 5. Technical and conforming amendments\n##### (a) Requirements To consult with or seek the concurrence\nFor any provision of law requiring an executive branch agency or independent agency to consult with or seek the concurrence of the FTC or the Chairman of the FTC, where such requirement relates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date, that requirement shall be transferred from the FTC or the Chairman of the FTC to the Attorney General.\n##### (b) Premerger notification filings\n**(1) FTC premerger notification filings**\nFor any provision of law requiring notification to the FTC, where such requirement relates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date, that requirement for notification to the FTC shall be waived.\n**(2) Department of Justice premerger notification filings**\nNothing in paragraph (b) may be construed as implying any change to the requirement for any required notification to the Attorney General.\n##### (c) Existing litigation or appeals\nNotwithstanding any other provision of law, the Attorney General shall not deny resources to the FTC or otherwise disrupt existing litigation or appeals that are ongoing on the day before the effective date.\n##### (d) Future actions of Attorney General\nNotwithstanding any other provision of law, nothing in this Act may be construed to limit the powers of the Attorney General to enforce the antitrust laws.\n##### (e) Future actions of the FTC\nNotwithstanding any other provision of law, the FTC shall not open new investigations or begin enforcement actions that relates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), except as explicitly allowed in this Act with the approval of the Attorney General and relating to an investigation, litigation, appeal, or consent decree that was ongoing or in place on the day before the effective date.\n#### 6. Effective date\nExcept as provided otherwise, this Act shall take effect on the start of the first fiscal year that is at least 90 days after the date of enactment of this Act.",
      "versionDate": "2025-01-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1059",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Agency Act",
      "type": "S"
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
        "updateDate": "2025-02-26T21:06:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr384",
          "measure-number": "384",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr384v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>One Agency Act</strong></p><p>This bill consolidates federal antitrust enforcement authority in one department by transferring the Federal Trade Commission's (FTC) antitrust functions, employees, assets, and funding to the Department of Justice (DOJ).<br/><br/>The bill provides a one-year period for DOJ to implement the transition and allows DOJ to extend the period once for an additional 180 days. During the transition period, DOJ may restructure the department's antitrust division and deputize FTC antitrust employees to investigate and prosecute antitrust violations on behalf of DOJ prior to the completion of the transfer of personnel from the FTC to DOJ.<br/><br/>DOJ is also authorized to require businesses to file annual or special reports about the business\u2019s organization, conduct, practices, management, and relationship to other businesses filing such reports.<br/><br/></p>"
        },
        "title": "One Agency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr384.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Agency Act</strong></p><p>This bill consolidates federal antitrust enforcement authority in one department by transferring the Federal Trade Commission's (FTC) antitrust functions, employees, assets, and funding to the Department of Justice (DOJ).<br/><br/>The bill provides a one-year period for DOJ to implement the transition and allows DOJ to extend the period once for an additional 180 days. During the transition period, DOJ may restructure the department's antitrust division and deputize FTC antitrust employees to investigate and prosecute antitrust violations on behalf of DOJ prior to the completion of the transfer of personnel from the FTC to DOJ.<br/><br/>DOJ is also authorized to require businesses to file annual or special reports about the business\u2019s organization, conduct, practices, management, and relationship to other businesses filing such reports.<br/><br/></p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr384"
    },
    "title": "One Agency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Agency Act</strong></p><p>This bill consolidates federal antitrust enforcement authority in one department by transferring the Federal Trade Commission's (FTC) antitrust functions, employees, assets, and funding to the Department of Justice (DOJ).<br/><br/>The bill provides a one-year period for DOJ to implement the transition and allows DOJ to extend the period once for an additional 180 days. During the transition period, DOJ may restructure the department's antitrust division and deputize FTC antitrust employees to investigate and prosecute antitrust violations on behalf of DOJ prior to the completion of the transfer of personnel from the FTC to DOJ.<br/><br/>DOJ is also authorized to require businesses to file annual or special reports about the business\u2019s organization, conduct, practices, management, and relationship to other businesses filing such reports.<br/><br/></p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr384"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr384ih.xml"
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
      "title": "One Agency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One Agency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To transfer antitrust enforcement from the Federal Trade Commission to the Attorney General, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:24Z"
    }
  ]
}
```
