# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1059?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1059
- Title: One Agency Act
- Congress: 119
- Bill type: S
- Bill number: 1059
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1059",
    "number": "1059",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "One Agency Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T22:25:41Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "WY"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "LA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1059is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1059\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Lee (for himself, Mr. Tillis , Ms. Lummis , Mr. Kennedy , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo transfer antitrust enforcement from the Federal Trade Commission to the Department of Justice, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Agency Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIt is the policy of the United States to promote the vigorous, effective, and efficient enforcement of the antitrust laws.\n**(2)**\nThe overlapping antitrust enforcement jurisdiction of the Department of Justice and the Federal Trade Commission has wasted taxpayer resources, hampered enforcement efforts, and caused uncertainty for businesses and consumers in the United States.\n**(3)**\nIt is preferable that primary Federal responsibility for enforcing the antitrust laws of the United States be given to a single entity, and the Department of Justice is best suited to do so.\n#### 3. Definitions\nIn this Act:\n**(1) Antitrust laws**\nThe term antitrust laws means\u2014\n**(A)**\nthe Sherman Act ( 15 U.S.C. 1 et seq. ); and\n**(B)**\nthe Clayton Act ( 15 U.S.C. 12 et seq. ).\n**(2) Effective date**\nThe term effective date means the date described in section 7.\n**(3) FTC**\nThe term FTC means the Federal Trade Commission.\n**(4) FTC antitrust action**\nThe term FTC antitrust action means any investigation, litigation, administrative proceeding, or other action of the FTC that\u2014\n**(A)**\nis supervised by an FTC antitrust unit; or\n**(B)**\nrelates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date.\n**(5) FTC antitrust assets**\nThe term FTC antitrust assets \u2014\n**(A)**\nmeans all electronic or tangible records and files relating to matters supervised, as well as any physical assets or equipment owned and used or retained, by an FTC antitrust unit; and\n**(B)**\ndoes not include any office space or leased facilities or equipment.\n**(6) FTC antitrust employee**\nThe term FTC antitrust employee means an individual who on the day before the effective date is employed by the FTC and assigned to an FTC antitrust unit.\n**(7) FTC antitrust funding**\nThe term FTC antitrust funding means all amounts appropriated before the effective date by an Act of Congress to the FTC that are designated, by Congress or the FTC for an FTC antitrust unit.\n**(8) FTC antitrust unit**\nThe term FTC antitrust unit means\u2014\n**(A)**\nthe Bureau of Competition of the FTC; and\n**(B)**\neach division of the Bureau of Economics of the FTC that is designated to work on FTC antitrust actions.\n**(9) Transition period**\nThe term transition period means the period beginning on the effective date and ending on the later of\u2014\n**(A)**\nthe date that is 1 year after the effective date; or\n**(B)**\nthe date that is 180 days after the date described in subparagraph (A), which may be extended by the Attorney General once for an additional 180 days, if the Attorney General determines that a period longer than the period described in subparagraph (A) is necessary to avoid harm to the interests of the United States or the effective enforcement of the antitrust laws.\n#### 4. Transfer of antitrust enforcement functions from the FTC to the Department of Justice\n##### (a) Transfer of actions\n**(1) In general**\nThere shall be transferred to the Attorney General all FTC antitrust actions, FTC antitrust employees, FTC antitrust assets, and FTC antitrust funding on the earlier of\u2014\n**(A)**\nthe date determined by the Attorney General under paragraph (2)(B); or\n**(B)**\nthe end of the transition period.\n**(2) Requirement**\nThe Attorney General, taking care to minimize disruption to ongoing enforcement matters and in consultation as necessary with the Office of Personnel Management, the General Services Administration, and the Chairman of the FTC, shall\u2014\n**(A)**\ntake all necessary actions to complete implementation of this Act before the end of the transition period; and\n**(B)**\ndetermine the dates certain, which may not be earlier than the effective date nor later than the end of the transition period, on which the transfers under paragraph (1) shall occur.\n**(3) Personnel**\n**(A) Assignment**\nAn FTC antitrust employee transferred to the Department of Justice under this Act shall be assigned to the Antitrust Division of the Department of Justice.\n**(B) Office space**\nOn the request of the Attorney General, and in consultation as necessary with the General Services Administration, the FTC shall allow the Department of Justice to use any office space or leased facilities previously used by FTC antitrust employees until such time as the Department of Justice may provide office space or facilities. After the transfer of FTC antitrust funding to the Department of Justice, the Department of Justice shall compensate the FTC for the costs of the use of such office space or leased facilities.\n**(C) Restructuring**\nNotwithstanding any other provision of law, the Attorney General is authorized to restructure the Antitrust Division of the Department of Justice before the expiration of the transition period, as the Attorney General determines is appropriate, to carry out the purposes of this Act and accomplish the efficient enforcement of the antitrust laws.\n**(4) Antitrust actions**\n**(A) In general**\nAs soon as is reasonably practicable during the transition period, all open investigations, studies, litigations, matters, or other proceedings being supervised by an FTC antitrust unit and relating to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date, shall be transferred to and assumed by the Department of Justice.\n**(B) Handling of FTC antitrust actions**\nAny FTC antitrust action that was initiated by the FTC and was unresolved as of the first day of the transition period shall be continued as the Attorney General determines is appropriate. The FTC shall have the power to deputize former FTC antitrust employees, with the consent of the Attorney General, to continue such FTC antitrust actions.\n**(C) Intervention**\nAny FTC antitrust action before a court of the United States that was initiated by the FTC and was unresolved as of the first day of the transition period, shall be continued as the Attorney General determines is appropriate. The FTC shall have the power to deputize former FTC antitrust employees, with the consent of the Attorney General, to continue such FTC antitrust actions.\n**(D) Consent decrees**\n**(i) In general**\nAt the end of the transition period, the Attorney General shall have sole authority to receive all reports as required under, enforce violations of, approve modifications to, or rescind any consent decree entered into by the FTC before the effective date that concerns conduct alleged to violate the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as in effect on the day before the effective date.\n**(ii) Administrative enforcement**\nIf determined necessary by the FTC and the Attorney General, the FTC shall have the power to deputize former FTC antitrust employees, with the consent of the Attorney General, to enforce and negotiate modifications of FTC consent decrees in effect on the day before the effective date in the administrative process of the FTC.\n**(5) Authority to conduct investigative studies**\n**(A) Reports of persons, partnerships, and corporations**\n**(i) In general**\nThe Attorney General may require, by general or special orders, persons, partnerships, and corporations, engaged in or whose business affects commerce to file with the Attorney General in such form as the Attorney General may prescribe annual or special reports or answers in writing to specific questions, furnishing to the Attorney General such information as the Attorney General may require as to the organization, business, conduct, practices, management, and relation to other corporations, partnerships, and individuals of the respective persons, partnerships, and corporations filing such reports or answers in writing.\n**(ii) Oath**\nReports and answers required under clause (i) shall\u2014\n**(I)**\nbe made under oath or otherwise as the Attorney General may prescribe;\n**(II)**\npertain solely to competition or the application of the antitrust laws; and\n**(III)**\nbe filed with the Attorney General within such reasonable period as the Attorney General may prescribe, unless additional time be granted in any case by the Attorney General.\n**(B) Publication of information or reports**\n**(i) In general**\nExcept as provided in clause (ii), the Attorney General\u2014\n**(I)**\nshall make public from time to time such portions of the information obtained by the Attorney General under this paragraph as are in the public interest;\n**(II)**\nmay make annual and special reports to Congress that include recommendations for additional legislation; and\n**(III)**\nshall provide for the publication of reports and decisions of the Attorney General in such form and manner as may be best adapted for public information and use.\n**(ii) Prohibition against publication of privileged or confidential information**\n**(I) In general**\nExcept as provided in subclause (II), the Attorney General shall not make public any trade secret or any commercial or financial information that is obtained from any person and that is privileged or confidential.\n**(II) Exception**\nThe Attorney General may disclose information described in subclause (I) to\u2014\n**(aa)**\nofficers and employees of appropriate Federal law enforcement agencies or to any officer or employee of any State law enforcement agency upon the prior certification of an officer of any such Federal or State law enforcement agency that such information will be maintained in confidence and will be used only for official law enforcement purposes; or\n**(bb)**\nany officer or employee of any foreign law enforcement agency under the same circumstances that making material available to foreign law enforcement agencies is permitted under section 21(b) of the Federal Trade Commission Act ( 15 U.S.C. 57b\u20132(b) ).\n**(6) Benefit of antitrust division**\nAll FTC antitrust assets and FTC antitrust funding transferred under this subsection shall be for the exclusive use and benefit of the Antitrust Division of the Department of Justice, except to the extent the FTC deputizes former FTC antitrust employees, with the consent of the Attorney General, to continue any FTC antitrust actions that are ongoing and unresolved before the effective date.\n##### (b) Transition period\n**(1) In general**\nExcept as provided in paragraph (2), beginning on the effective date, the FTC may not\u2014\n**(A)**\nhire or assign an employee to an FTC antitrust unit;\n**(B)**\nopen a new investigation or matter within an FTC antitrust unit or relating to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act;\n**(C)**\nwithout the approval of the Attorney General, enter into a consent decree, enter into a settlement agreement, or otherwise resolve an FTC antitrust action; or\n**(D)**\ninitiate a new FTC antitrust action.\n**(2) Enforcement on behalf of the Department of Justice**\nNotwithstanding paragraph (1), during the transition period, the Attorney General may deputize an FTC antitrust employee to investigate or prosecute an alleged violation of the antitrust laws on behalf of the Department of Justice before the completion of the transfer of personnel under subsection (a).\n**(3) Same rights and obligations**\n**(A) In general**\nNotwithstanding any other provision of law, during the transition period all Department of Justice employees under the supervision of the Attorney General shall have the same rights and obligations with respect to confidential information submitted to the FTC as FTC antitrust employees on the day before the effective date.\n**(B) Rule of construction**\nNothing in this paragraph may be construed as implying any change to the rights and obligations described in subparagraph (A) as a result of this Act.\n##### (c) Agreements\nThe Attorney General, in consultation with the Chairman of the FTC, shall\u2014\n**(1)**\nreview any agreements between the FTC and any other Federal agency or any foreign law enforcement agency; and\n**(2)**\nbefore the end of the transition period, seek to amend, transfer, or rescind such agreements as necessary and appropriate to carry out this Act, endeavoring to complete such amendment, transfer, or rescindment with all due haste.\n##### (d) Rules\nThe Attorney General shall, pursuant to section 7A of the Clayton Act ( 15 U.S.C. 18a ) and in accordance with section 553 of title 5, United States Code, prescribe or amend any rules as necessary to carry out the Clayton Act.\n#### 5. Transfer of functions\n##### (a) In general\nAny requirement that an agency of the executive branch or an independent agency consult with or seek the concurrence of the FTC or the Chairman of the FTC, where such requirement relates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) as in effect on the day before the effective date, shall be deemed transferred from the FTC or the Chairman of the FTC to the Department of Justice or the Attorney General.\n##### (b) Premerger notification filings\n**(1) FTC premerger notification filings**\nWith respect to any requirement that an agency or entity provide notification to the FTC, where such requirement relates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) as in effect on the day before the effective date, that notification shall be submitted to the Attorney General.\n**(2) Department of Justice premerger notification filings**\nNothing in paragraph (1) may be construed as implying any change to the requirement for any required notification to the Attorney General.\n##### (c) Existing litigation or appeals\nNotwithstanding any other provision of law, the Attorney General shall not deny resources to the FTC or otherwise disrupt existing litigation or appeals that are ongoing on the day before the effective date.\n##### (d) Future actions of Attorney General\nNotwithstanding any other provision of law, nothing in this Act may be construed to limit the powers of the Attorney General to enforce the antitrust laws.\n##### (e) Future actions of the FTC\nNotwithstanding any other provision of law, the FTC shall not open a new investigation or begin an enforcement action that relates to the antitrust laws or unfair methods of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), except as explicitly allowed under this Act with the approval of the Attorney General and relating to an investigation, litigation, appeal, or consent decree that was ongoing or in place on the day before the effective date.\n#### 6. Technical and conforming amendments\n##### (a) Clayton Act\nThe Clayton Act ( 15 U.S.C. 12 et seq. ) is amended\u2014\n**(1)**\nin section 2 ( 15 U.S.C. 13 )\u2014\n**(A)**\nin subsection (a), by striking Federal Trade Commission and inserting Attorney General of the United States ; and\n**(B)**\nin subsection (b), by striking Commission and inserting Attorney General of the United States ;\n**(2)**\nin section 5(a) ( 15 U.S.C. 16(a) ), in the second sentence, by striking , except that, in any action or proceeding brought under the antitrust laws, collateral estoppel effect shall not be given to any finding made by the Federal Trade Commission under the antitrust laws or under section 5 of the Federal Trade Commission Act which could give rise to a claim for relief under the antitrust laws ;\n**(3)**\nin section 7 ( 15 U.S.C. 18 )\u2014\n**(A)**\nin the first undesignated paragraph, by striking and no person subject to the jurisdiction of the Federal Trade Commission shall acquire the whole or any part of the assets of another person engaged also in commerce or in any activity affecting commerce ; and\n**(B)**\nin the second undesignated paragraph, by striking and no person subject to the jurisdiction of the Federal Trade Commission shall acquire the whole or any part of the assets of one or more persons engaged in commerce or in any activity affecting commerce ;\n**(4)**\nin section 7A ( 15 U.S.C. 18a )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)(A), in the matter preceding clause (i), by striking the Federal Trade Commission and ; and\n**(ii)**\nin paragraph (2), by striking Federal Trade Commission and the ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (6), by striking the Federal Trade Commission and ; and\n**(ii)**\nin paragraph (8), by striking the Federal Trade Commission and ;\n**(C)**\nin subsection (d)\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking Federal Trade Commission, with the concurrence of the Attorney General and and inserting Attorney General of the United States ; and\n**(ii)**\nin paragraph (1), by striking the Federal Trade Commission and ;\n**(D)**\nin subsection (e)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin subparagraph (A), by striking Federal Trade Commission or the ; and\n**(II)**\nin subparagraph (B), by striking and the Federal Trade Commission shall each and inserting shall ; and\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nby striking Federal Trade Commission or the ;\n**(II)**\nby striking its or\u2019 ;\n**(III)**\nby striking the Federal Trade Commission or each place the term appears; and\n**(IV)**\nby striking , as the case may be, ;\n**(E)**\nin subsection (f)\u2014\n**(i)**\nby striking the Federal Trade Commission, alleging that a proposed acquisition violates section 7 of this Act or section 5 of the Federal Trade Commission Act, or an action is filed by ; and\n**(ii)**\nby striking the Federal Trade Commission or ;\n**(F)**\nin subsection (g)(2), in the matter following subparagraph (C), by striking the Federal Trade Commission or ;\n**(G)**\nin subsection (h), by striking or the Federal Trade Commission ; and\n**(H)**\nin subsection (i)\u2014\n**(i)**\nin paragraph (1), by striking the Federal Trade Commission or each place the term appears; and\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nby striking or the Federal Trade Commission ; and\n**(J)**\nby striking , the Federal Trade Commission Act, ; and\n**(5)**\nin section 8(a)(5) ( 15 U.S.C. 19(a)(5) ), in the second sentence, by striking Federal Trade Commission and inserting Attorney General of the United States .\n##### (b) Charitable Gift Annuity Antitrust Relief Act of 1995\nSection 3(1) of the Charitable Gift Annuity Antitrust Relief Act of 1995 ( 15 U.S.C. 37a(1) ) is amended by striking , except that such term includes section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that such section 5 applies to unfair methods of competition .\n##### (c) Pension Funding Equity Act of 2004\nSection 207(b)(1)(A)(i) of the Pension Funding Equity Act of 2004 ( 15 U.S.C. 37b(b)(1)(A)(i) ) is amended by striking , except that such term includes section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent such section 5 applies to unfair methods of competition .\n##### (d) Federal Trade Commission Act\nThe Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) is amended\u2014\n**(1)**\nin section 5 ( 15 U.S.C. 45 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking methods of competition in or affecting commerce, and unfair ;\n**(ii)**\nby striking paragraph (3); and\n**(iii)**\nby redesignating paragraph (4) as paragraph (3);\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin the first sentence, by striking unfair method of competition or ; and\n**(ii)**\nin the fifth sentence\u2014\n**(I)**\nby striking the method of competition or ; and\n**(II)**\nby striking method of competition or such ;\n**(C)**\nin subsection (c)\u2014\n**(i)**\nin the first sentence\u2014\n**(I)**\nby striking method of competition or ; and\n**(II)**\nby striking method of competition or the ; and\n**(ii)**\nin the third sentence, by striking or to competitors ;\n**(D)**\nby striking subsection (e);\n**(E)**\nin subsection (g), by striking paragraph (4); and\n**(F)**\nin subsection (n), in the first sentence, by striking or to competition ;\n**(2)**\nin section 6 ( 15 U.S.C. 46 )\u2014\n**(A)**\nby striking subsections (c) through (e) and (i);\n**(B)**\nby redesignating\u2014\n**(i)**\nsubsections (f), (g), and (h) as subsections (c) through (e), respectively; and\n**(ii)**\nsubsections (j) through (l) as subsections (f) through (h), respectively;\n**(C)**\nin subsection (f)(1), as so redesignated, by striking other than Federal antitrust laws (as defined in section 12(5) of the International Antitrust Enforcement Assistance Act of 1994 ( 15 U.S.C. 6211(5) )), ; and\n**(D)**\nin subsection (h)(2), as so redesignated, in the matter preceding subparagraph (A), by striking or competition ;\n**(3)**\nby repealing section 7 ( 15 U.S.C. 47 );\n**(4)**\nin section 11 ( 15 U.S.C. 51 ), by striking antitrust Acts or the each place the term appears;\n**(5)**\nin section 18 ( 15 U.S.C. 57a(a)(2) ), by striking the second sentence;\n**(6)**\nin section 20 ( 15 U.S.C. 57b\u20131 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (2), by striking or in any antitrust violations ;\n**(ii)**\nin paragraph (3), by striking or any provisions relating to antitrust violations ;\n**(iii)**\nin paragraph (7), by striking or any antitrust violation ; and\n**(iv)**\nby striking paragraph (8);\n**(B)**\nin subsection (c)(1), by striking or to antitrust violations, ; and\n**(C)**\nin subsection (j)(1), by striking , any proceeding under section 11(b) of the Clayton Act ( 15 U.S.C. 21(b) ), ;\n**(7)**\nin section 21(b)(6) ( 15 U.S.C. 57b\u20132(b)(6) ), in the matter following subparagraph (D), by striking paragraphs (5) and (7) and inserting paragraphs (4) and (6) ; and\n**(8)**\nin section 21A ( 15 U.S.C. 57b\u20132a )\u2014\n**(A)**\nby striking subsection (f);\n**(B)**\nby redesignating subsection (g) as subsection (f);\n**(C)**\nin subsection (f), as so redesignated, by striking subsection (g) each place the term appears and inserting subsection (f) ; and\n**(D)**\nin section 24 ( 15 U.S.C. 57b\u20135(a) ), by striking for any conduct which, because of the provisions of the Act entitled An Act to authorize association of producers of agricultural products , approved February 18, 1922 ( 7 U.S.C. 291 et seq. , commonly known as the Capper-Volstead Act), is not a violation of any of the antitrust Acts or this Act .\n##### (e) Webb-Pomerene Act\nThe Webb-Pomerene Act ( 15 U.S.C. 61 et seq. ) is amended\u2014\n**(1)**\nby repealing section 4 ( 15 U.S.C. 64 ); and\n**(2)**\nin section 5\u2014\n**(A)**\nin the first undesignated paragraph\u2014\n**(i)**\nin the first sentence, by striking Federal Trade Commission and inserting Attorney General of the United States ; and\n**(ii)**\nin the second sentence, by striking commission each place the term appears and inserting Attorney General of the United States ;\n**(B)**\nin the second undesignated paragraph\u2014\n**(i)**\nin the first sentence, by striking Federal Trade Commission and inserting Attorney General of the United States ; and\n**(ii)**\nby striking the third sentence; and\n**(C)**\nby striking the third undesignated paragraph.\n##### (f) Wool Products Labeling Act of 1939\nThe Wool Products Labeling Act of 1939 ( 15 U.S.C. 68 et seq. ) is amended\u2014\n**(1)**\nby striking an unfair method of competition, and each place the term appears; and\n**(2)**\nin section 68g(b), by striking an unfair method of competition and .\n##### (g) Fur Products Labeling Act\nThe Fur Products Labeling Act ( 15 U.S.C. 69 et seq. ) is amended by striking an unfair method of competition, and each place the term appears.\n##### (h) Textile Fiber Products Identification Act\nThe Textile Fiber Products Identification Act ( 15 U.S.C. 70 et seq. ) is amended\u2014\n**(1)**\nby striking an unfair method of competition, and each place the term appears; and\n**(2)**\nin section 3 ( 15 U.S.C. 70a ), by striking an unfair method of competition and each place the term appears.\n##### (i) Antitrust Civil Process Act\nSection 4(d) of the Antitrust Civil Process Act ( 15 U.S.C. 1313(d) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking (1) Whoever and inserting Whoever ; and\n**(2)**\nby striking paragraph (2).\n##### (j) International Antitrust Enforcement Assistance Act of 1994\nThe International Antitrust Enforcement Assistance Act of 1994 ( 15 U.S.C. 6201 et seq. ) is amended\u2014\n**(1)**\nin section 2 ( 15 U.S.C. 6201 ), in the matter preceding paragraph (1), by striking and the Federal Trade Commission ;\n**(2)**\nin section 3(b) ( 15 U.S.C. 6202(b) ), by striking and the Commission may, using their respective authority to investigate possible violations of the Federal antitrust laws, and inserting may ;\n**(3)**\nin section 5(1) ( 15 U.S.C. 6204(1) ), by striking or the Commission each place the term appears;\n**(4)**\nin section 6 ( 15 U.S.C. 6205 )\u2014\n**(A)**\nby striking or the Commission ; and\n**(B)**\nby striking 6(f) and inserting 6(c) ;\n**(5)**\nin section 7 ( 15 U.S.C. 6206 )\u2014\n**(A)**\nby striking , with the concurrence of the Commission, each place the term appears; and\n**(B)**\nin subsection (c)(2)(B), by striking and the Commission ;\n**(6)**\nin section 8 ( 15 U.S.C. 6207 )\u2014\n**(A)**\nby striking Neither the Attorney General nor the Commission may each place the term appears and inserting The Attorney General may not ;\n**(B)**\nin subsection (a), by striking or the Commission, as the case may be, ;\n**(C)**\nin subsection (b), by striking or the Commission ; and\n**(D)**\nin subsection (c)\u2014\n**(i)**\nby striking or the Commission ; and\n**(ii)**\nby striking or the Commission, as the case may be, ;\n**(7)**\nin section 10 ( 15 U.S.C. 6209 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking , the Commission, ; and\n**(ii)**\nby striking (a) In General.\u2014The and inserting The ; and\n**(B)**\nby striking subsection (b);\n**(8)**\nin section 12 ( 15 U.S.C. 6211 )\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A)\u2014\n**(I)**\nby striking and the Commission jointly determine and inserting determines ;\n**(II)**\nby striking jointly ; and\n**(III)**\nby striking and the Commission ;\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby striking and the Commission each place the term appears; and\n**(II)**\nby striking provide and inserting provides ;\n**(iii)**\nin subparagraph (E)(ii), in the matter preceding subclause (I), by striking or the Commission, as the case may be, ;\n**(iv)**\nin subparagraph (F)\u2014\n**(I)**\nby striking or the Commission ; and\n**(II)**\nby striking or the Commission, respectively, ; and\n**(v)**\nin subparagraph (H)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking or the Commission ; and\n**(bb)**\nby striking or the Commission, respectively, ; and\n**(II)**\nin clause (ii), by striking or the Commission each place the term appears;\n**(B)**\nby striking paragraph (4);\n**(C)**\nby redesignating paragraphs (5) through (9) as paragraphs (4) through (8), respectively; and\n**(D)**\nin paragraph (4), as so redesignated, by striking but also includes section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that such section 5 applies to unfair methods of competition ; and\n**(9)**\nin section 13 ( 15 U.S.C. 6212 )\u2014\n**(A)**\nby striking and the Commission are and inserting is ; and\n**(B)**\nby striking or the Commission, respectively, .\n##### (k) Medicare Prescription Drug, Improvement, and Modernization Act of 2003\nSubtitle B of title XI of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( Public Law 108\u2013173 ; 117 Stat. 2461) is amended\u2014\n**(1)**\nin the subtitle heading, by striking Federal Trade Commission and inserting Antitrust ;\n**(2)**\nin section 1111 ( 21 U.S.C. 355 note)\u2014\n**(A)**\nby striking paragraph (8); and\n**(B)**\nby redesignating paragraphs (9) through (12) as paragraphs (8) through (11), respectively;\n**(3)**\nin section 1112(c) ( 21 U.S.C. 355 note), by striking and the Commission each place the term appears;\n**(4)**\nin section 1113 ( 21 U.S.C. 355 note), by striking and the Commission ;\n**(5)**\nin section 1114 ( 21 U.S.C. 355 note), by striking or the Commission ;\n**(6)**\nin section 1115 ( 21 U.S.C. 355 note)\u2014\n**(A)**\nin subsection (a), by striking , or brought by the Commission in accordance with the procedures established in section 16(a)(1) of the Federal Trade Commission Act ( 15 U.S.C. 56(a) ) ; and\n**(B)**\nin subsection (b), by striking or the Commission ;\n**(7)**\nin section 1116 ( 21 U.S.C. 355 note), in the matter preceding paragraph (1), by striking Commission, with the concurrence of the Attorney General and inserting Attorney General ; and\n**(8)**\nin section 1117 ( 21 U.S.C. 355 note), by striking or the Commission each place the term appears.\n#### 7. Effective date\nExcept as provided otherwise, this Act and the amendments made by this Act shall take effect on the start of the first fiscal year that is at least 90 days after the date of enactment of this Act.",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-01-14",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "384",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Agency Act",
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
        "updateDate": "2025-04-03T11:35:34Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1059is.xml"
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
      "title": "One Agency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T02:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "One Agency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to transfer antitrust enforcement from the Federal Trade Commission to the Department of Justice, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:37Z"
    }
  ]
}
```
