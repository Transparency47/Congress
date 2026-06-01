# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1536
- Title: Building Ships in America Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1536
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-06-04T14:59:37Z
- Update date including text: 2025-06-04T14:59:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1536",
    "number": "1536",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Building Ships in America Act of 2025",
    "type": "S",
    "updateDate": "2025-06-04T14:59:37Z",
    "updateDateIncludingText": "2025-06-04T14:59:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T19:29:07Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "IN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AK"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1536is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1536\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Kelly (for himself, Mr. Young , Ms. Murkowski , Ms. Baldwin , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to support the national defense and economic security of the United States by supporting vessels, ports, and shipyards of the United States and the United States maritime workforce through tax policy.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Building Ships in America Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. United States vessel investment credit.\nSec. 3. Certain payments for maritime security excluded from gross income.\nSec. 4. Elimination of 30-day limitation on domestic operations.\nSec. 5. Qualifying shipping activities.\nSec. 6. Qualifying vessel.\nSec. 7. Credit for construction of shipyard facilities.\nSec. 8. Tax incentives relating to merchant marine capital construction funds.\nSec. 9. Exemption of student incentive payment agreements from gross income.\nSec. 10. Maritime fuel tax parity.\nSec. 11. Treatment of maritime prosperity zones as opportunity zones.\n#### 2. United States vessel investment credit\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. United States vessel investment credit (a) In general For purposes of section 46, the United States Vessel Investment credit for any taxable year is an amount equal to the applicable percentage of any qualified investment for such taxable year with respect to any qualified vessel. (b) Applicable percentage For purposes of subsection (a), the applicable percentage with respect to any qualified vessel shall be an amount equal to the sum of\u2014 (1) 33 percent, plus (2) in the case of any qualified vessel for which the owner of such vessel will, as part of the agreement described in subsection (d)(1)(F) and for the duration of such agreement, obtain protection and indemnity insurance with respect to such vessel from an insurance company that is domiciled and headquartered in the United States and is an underwriter that is approved by the Maritime Administrator, 5 percent, plus (3) in the case of any qualified vessel which is classified by and designed in accordance with the rules of the American Bureau of Shipping or any other classification society headquartered in the United States and recognized by the Secretary of the department in which the Coast Guard is operating in accordance with section 3316 of title 46, United States Code, 2 percent. (c) Qualified investment For purposes of subsection (a), the qualified investment with respect to any qualified vessel is equal to the amount paid or incurred by the taxpayer in connection with the construction, repowering, or reconstruction of such vessel\u2014 (1) in a shipyard of the United States, and (2) by an entity which is not a foreign entity of concern. (d) Qualified vessel (1) In general For purposes of this section, the term qualified vessel means a cargo vessel\u2014 (A) which is a United States flag vessel (as defined in section 1355), (B) which, in the case of any repowering or reconstruction of such vessel, was originally constructed in the United States, (C) which operates in providing transportation in the United States foreign trade (as such term is defined in section 1355(a)), (D) which is not a passenger vessel, as defined in section 2101 of title 46, United States Code, (E) which is\u2014 (i) a bulk carrier vessel, (ii) a tanker vessel, (iii) a roll-on/roll-off vessel, (iv) a container vessel, (v) a multi-purpose vessel, (vi) a cable vessel, (vii) a heavy-lift vessel, or (viii) any other type of vessel determined appropriate by the Maritime Administrator, (F) which, pursuant to an agreement between the taxpayer and the Maritime Administrator, operates as a vessel of the United States for a period of not less than 10 years, (G) which has entered into an emergency preparedness agreement under section 53107 or 53407 of title 46, United States Code, or a contingency agreement under section 53207 of such title, or has otherwise entered into a voluntary agreement and plan of action with the Administrator of the Maritime Administration as authorized under section 708(c) of the Defense Production Act of 1950 (50 U.S.C. 4558(c)), and (H) the construction of which begins before January 1, 2033. (2) Exclusion related to foreign entities of concern The term qualified vessel shall not include a vessel which\u2014 (A) is, or was previously, owned or operated by a foreign entity of concern, (B) was constructed, repowered, or reconstructed in a shipyard which is owned or operated by a foreign entity of concern, or (C) was registered as a vessel of a foreign country of concern at any time prior to being placed in service by the taxpayer. (e) Definitions For purposes of this section\u2014 (1) Foreign country of concern The term foreign country of concern means\u2014 (A) a country that is a covered nation (as defined in section 4872(d) of title 10, United States Code), and (B) any country that the Maritime Administrator, in consultation with the Secretary of Defense, the Secretary of State, the Director of National Intelligence, and the Chair of the Federal Maritime Commission, determines to be engaged in conduct that is detrimental to the national security or foreign policy of the United States. (2) Foreign entity The term foreign entity \u2014 (A) means\u2014 (i) a government of a foreign country or a foreign political party, as those terms are defined in section 1 of the Foreign Agents Registration Act of 1938, as amended (22 U.S.C. 611), (ii) a natural person who is not a lawful permanent resident of the United States, a citizen of the United States, or any other protected individual (as such term is defined in section 274B(a)(3) of the Immigration and Nationality Act (8 U.S.C. 1324b(a)(3))), or (iii) a partnership, association, corporation, organization, or other combination of persons organized under the laws of or having its principal place of business in a foreign country, and (B) includes\u2014 (i) any person (including an owner or operator of a vessel) owned by, controlled by, or subject to the direction of an entity listed in subparagraph (A), (ii) any person, wherever located, who acts as an agent, representative, or employee of an entity listed in subparagraph (A), (iii) any person who acts in any other capacity at the order, request, or under the direction or control, of an entity listed in subparagraph (A), or of a person whose activities are directly or indirectly supervised, directed, controlled, financed, or subsidized in whole or in major part by an entity listed in subparagraph (A), (iv) any person who directly or indirectly through any contract, arrangement, understanding, relationship, or otherwise, owns 25 percent or more of the equity interests of an entity listed in subparagraph (A), (v) any person with significant responsibility to control, manage, or direct an entity listed in subparagraph (A), (vi) any person, wherever located, who is a citizen or resident of a country controlled by an entity listed in subparagraph (A), or (vii) any corporation, partnership, association, or other organization organized under the laws of a country controlled by an entity listed in subparagraph (A). (3) Foreign entity of concern The term foreign entity of concern means any foreign entity that is\u2014 (A) designated as a foreign terrorist organization by the Secretary of State under section 219 of the Immigration and Nationality Act (8 U.S.C. 1189), (B) included on the list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury, (C) owned by, controlled by, or subject to the jurisdiction or direction of a government of a foreign country of concern, (D) alleged by the Attorney General to have been involved in activities for which a conviction was obtained under\u2014 (i) chapter 37 of title 18, United States Code (commonly known as the Espionage Act ) (18 U.S.C. 792 et seq.), (ii) section 951 or 1030 of title 18, United States Code, (iii) chapter 90 of title 18, United States Code (commonly known as the Economic Espionage Act of 1996 ), (iv) the Arms Export Control Act (22 U.S.C. 2751 et seq.), (v) section 224, 225, 226, 227, or 236 of the Atomic Energy Act of 1954 (42 U.S.C. 2274, 2275, 2276, 2277, and 2284), (vi) the Export Control Reform Act of 2018 (50 U.S.C. 4801 et seq.), or (vii) the International Emergency Economic Powers Act (50 U.S.C. 1701 et seq.), (E) designated by the Federal Maritime Commission as a controlled carrier under chapter 407 of title 46, United States Code, (F) found by the Federal Maritime Commission to be practicing unfavorable conditions in foreign trade under chapter 421 or 423 of title 46, United States Code, or (G) determined by the Maritime Administrator, in consultation with the Secretary of Defense, the Secretary of State, the Director of National Intelligence, and the Chair of the Federal Maritime Commission, to be engaged in unauthorized conduct that is detrimental to the national security or foreign policy of the United States. (f) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). (g) Regulations The Secretary, in consultation with the Maritime Administrator, shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including any regulations or guidance which may be necessary or appropriate to recapture the benefit of any credit determined under this section with respect to any qualified vessel, or any increase in the applicable percentage under subsection (b) with respect to any qualified vessel, in the case of any taxpayer which fails to comply with the terms of the agreement described in subsection (d)(1)(F) with respect to such qualified vessel. .\n##### (b) Conforming amendments\n**(1)**\nSection 46 of the Internal Revenue Code of 1986, as amended by section 13702(b)(1) of Public Law 117\u2013169, is amended\u2014\n**(A)**\nin paragraph (6), by striking and at the end,\n**(B)**\nin paragraph (7), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(8) the United States Vessel Investment credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code, as amended by section 13702(b)(2) of Public Law 117\u2013169, is amended\u2014\n**(A)**\nin clause (vii), by striking and at the end,\n**(B)**\nin clause (viii), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(ix) with respect to any qualified vessel (as defined in section 48F(d)), the portion of the basis of such vessel attributable to amounts paid or incurred by the taxpayer in connection with the construction, repowering, or reconstruction of such vessel. .\n**(3)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. United States Vessel Investment credit. .\n##### (c) Recapture for failure To operate as a vessel of the United States\nSection 50(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (4), by striking or any applicable transaction to which paragraph (3)(A) applies and inserting any applicable transaction to which paragraph (3)(A) applies, or any violation to which paragraph (6)(A) applies ,\n**(2)**\nby redesignating paragraph (6) as paragraph (7),\n**(3)**\nby inserting after paragraph (5) the following new paragraph:\n(6) Failure to operate qualified vessel as a vessel of the United States (A) In general If an applicable taxpayer violates any of the requirements of the agreement described in section 48F(d)(1)(F) during the duration of such agreement with respect to any investment credit property which is eligible for the United States Vessel Investment credit under section 48F(a), then the tax under this chapter for the taxable year in which such violation occurs shall be increased by 100 percent of the aggregate decrease in the credits allowed under section 38 for all prior taxable years which would have resulted solely from reducing to zero any credit determined under section 46 which is attributable to the United States Vessel Investment credit under section 48F(a) with respect to such property. (B) Exception Subparagraph (A) shall not apply if the applicable taxpayer demonstrates to the satisfaction of the Secretary and the Maritime Administrator that the taxpayer is in compliance with the agreement described in section 48F(d)(1)(F) within 30 days of a determination and notice by the Secretary. (C) Regulations and guidance The Secretary shall issue such regulations or other guidance as the Secretary determines necessary or appropriate to carry out the purposes of this paragraph, including regulations or other guidance which provide for requirements for recordkeeping or information reporting for purposes of administering the requirements of this paragraph. , and\n**(4)**\nin paragraph (7) (as redesignated by paragraph (2))\u2014\n**(A)**\nin subparagraph (C), by striking or (3) and inserting (3), or (4) , and\n**(B)**\nby striking subparagraph (E) and inserting the following:\n(E) Applicable taxpayer For purposes of this subsection, the term applicable taxpayer means any taxpayer who has been allowed\u2014 (i) for purposes of paragraph (3), a credit under section 48D(a) for any prior taxable year, or (ii) for purposes of paragraph (6), a credit under section 48F(a) for any prior taxable year. .\n##### (d) Elective payment and transfer of credit\n**(1) Elective payment**\nSection 6417 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subsection (b), by adding at the end the following:\n(13) The United States Vessel Investment credit under section 48F. , and\n**(B)**\nin subsection (d)(1)\u2014\n**(i)**\nin subparagraph (E), by striking (C), or (D) each place it appears and inserting (C), (D), or (E) ,\n**(ii)**\nby redesignating subparagraph (E) (as amended by clause (i)) as subparagraph (F), and\n**(iii)**\nby inserting after subparagraph (D) the following:\n(E) Election with respect to United States vessel investment credit If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has made a qualified investment with respect to any qualified vessel (as defined in section 48F), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(13). .\n**(2) Transfer**\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(xii) The United States Vessel Investment credit under section 48F. .\n##### (e) Exception relating to alternative tax on qualifying shipping activities\nSection 1357(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1), by striking paragraph (2) and inserting paragraph (2) or (4) , and\n**(2)**\nby adding at the end the following:\n(4) Exception for United States vessel investment credit Paragraph (1) shall not apply with respect to any credit allowed to the taxpayer under section 48F. .\n##### (f) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2025.\n#### 3. Certain payments for maritime security excluded from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new subsection:\n139J. Maritime security payments (a) In general Gross income shall not include any payment made pursuant to\u2014 (1) section 53106 of title 46, United States Code, (2) section 53206 of such title, (3) section 53406 of such title, (4) section 54101 of such title, or (5) section 54301 of such title. (b) Denial of double benefit No deduction or credit shall be allowed for, or by reason of, any expenditure to the extent of the amount excluded under subsection (a) for any payment which was provided with respect to such expenditure. The adjusted basis of any property shall be reduced by the amount excluded under subsection (a) which was provided with respect to such property. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Maritime security payments. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 4. Elimination of 30-day limitation on domestic operations\n##### (a) In general\nSection 1355 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (f), by striking paragraph (4), and\n**(2)**\nin subsection (g)(2), by striking subparagraph (D).\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.\n#### 5. Qualifying shipping activities\nSection 1356(b) of the Internal Revenue Code of 1986 (relating to qualifying shipping activities) is amended by striking activities in operating and inserting the carriage of goods (as defined in section 1 of the Carriage of Goods by Sea Act (46 U.S.C. 30701 note)) by .\n#### 6. Qualifying vessel\nSection 1355(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking paragraph (4) and inserting the following:\n(4) Qualifying vessel The term qualifying vessel means a vessel which is\u2014 (A) self-propelled (or a combination self-propelled and non-self-propelled), (B) a United States flag vessel or a United States-owned foreign flag vessel, (C) either\u2014 (i) a vessel designed primarily for use on the high seas which has a draft of more than 12 feet, or (ii) not less than 6,000 deadweight tons, and (D) used exclusively in the United States foreign trade during the period that the election under this subchapter is in effect. , and\n**(2)**\nby adding at the end the following:\n(8) United States-owned foreign flag vessel The term United States-owned foreign flag vessel means any vessel which\u2014 (A) is documented under the laws of a country (other than the United States) or a foreign registry which is not a foreign country of concern (as defined in section 48F(e)), (B) is owned by a person which\u2014 (i) (I) is a citizen of the United States (as determined under section 50501 of title 46, United States Code), or (II) is controlled (within the meaning of section 954(d)(3)) by a citizen of the United States (as so determined), and (ii) owns a fleet of United States flag vessels, (C) is strategically and commercially managed from within the United States, and (D) has entered into an emergency preparedness agreement under section 53107 or 53407 of title 46, United States Code, or a contingency agreement under section 53207 of such title, or has otherwise entered into a voluntary agreement and plan of action with the Maritime Administrator as authorized under section 708(c) of the Defense Production Act of 1950 (50 U.S.C. 4558(c)). .\n#### 7. Credit for construction of shipyard facilities\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986, as amended by section 2(a), is amended by inserting after section 48F the following new section:\n48G. Credit for construction of shipyard facilities (a) In general For purposes of section 46, the shipyard investment tax credit for any taxable year is an amount equal to 25 percent of the qualified investment for such taxable year with respect to any qualified shipyard facility of a taxpayer described in section 48D(c)(1). (b) Qualified investment (1) In general For purposes of subsection (a), the qualified investment with respect to any qualified shipyard facility for any taxable year is the basis of any qualified property placed in service by the taxpayer during such taxable year which is part of a qualified shipyard facility. (2) Qualified property The term qualified property shall have the same meaning given such term in section 48D(b)(2), except that subparagraph (A)(iv) of such section shall be applied by substituting qualified shipyard facility for advanced manufacturing facility . (3) Qualified shipyard facility For purposes of this section, the term qualified shipyard facility means a facility\u2014 (A) which is located within the United States (including any territory or possession of the United States), and (B) for which the primary purpose is\u2014 (i) constructing or repairing commercial or military oceangoing vessels, (ii) manufacturing components which are critical (as determined by the Secretary, in consultation with the Secretary of the Navy and the Maritime Administrator) to the operation of commercial or military oceangoing vessels, or (iii) manufacturing equipment which is used to produce or repair commercial or military oceangoing vessels. (4) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). (c) Denial of double benefit This section shall not apply to any property placed in service by the taxpayer during the taxable year if a credit was allowed under section 48F to such taxpayer during such taxable year. (d) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. (e) Termination of credit The credit allowed under this section shall not apply to property placed in service after December 31, 2032. .\n##### (b) Conforming amendments\n**(1)**\nSection 46 of the Internal Revenue Code of 1986, as amended by section 2(b)(1), is amended\u2014\n**(A)**\nin paragraph (7), by striking and at the end,\n**(B)**\nin paragraph (8), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(9) the shipyard investment tax credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code, as amended by section 2(b)(2), is amended\u2014\n**(A)**\nin clause (viii), by striking and at the end,\n**(B)**\nin clause (ix), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(x) the basis of any qualified property (as defined in subsection (b)(2) of section 48G) which is part of a qualified shipyard facility (as defined in subsection (b)(3) of such section). .\n**(3)**\nSection 50(a)(2)(E) of such Code, as amended by section 13702(b) of Public Law 117\u2013169, is amended by striking or 48E(e) and inserting 48E(e), or 48G(b)(4) .\n**(4)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code, as amended by section 2(b)(3), is amended by inserting after the item relating to section 48F the following new item:\nSec. 48G. Shipyard investment tax credit. .\n##### (c) Elective payment and transfer of credit\n**(1) Elective payment**\nSection 6417 of the Internal Revenue Code of 1986, as amended by section 2, is amended\u2014\n**(A)**\nin subsection (b), by adding at the end the following:\n(14) The shipyard investment tax credit under section 48G. , and\n**(B)**\nin subsection (d)(1)\u2014\n**(i)**\nin subparagraph (F), by striking (D), or (E) each place it appears and inserting (D), (E), or (F) ,\n**(ii)**\nby redesignating subparagraph (F) (as amended by clause (i)) as subparagraph (G), and\n**(iii)**\nby inserting after subparagraph (E) the following:\n(F) Election with respect to the shipyard investment tax credit If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has placed in service any qualified property which is part of a qualified shipyard facility (as defined in section 48G), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(14). .\n**(2) Transfer**\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986, as amended by section 2, is amended by adding at the end the following:\n(xiii) The shipyard investment tax credit under section 48G. .\n##### (d) Exception relating to alternative tax on qualifying shipping activities\nParagraph (4) of section 1357(c) of the Internal Revenue Code of 1986, section 2(e), is amended to read as follows:\n(4) Exception for United States vessel investment credit and shipyard investment tax credit Paragraph (1) shall not apply with respect to any credit allowed to the taxpayer under section 48F or 48G. .\n##### (e) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2025.\n#### 8. Tax incentives relating to merchant marine capital construction funds\n##### (a) In general\nSection 7518 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) In general The amount deposited in a fund established under chapter 535 of title 46 of the United States Code (hereinafter in this section referred to as a capital construction fund ) for a taxable year may not exceed the amount specified in the agreement under section 53503(a) of such title, which shall be an amount that is related to a commitment to invest the revenue from the capital construction fund into funding the construction of new vessels or funding cargo handling equipment. ,\n**(B)**\nin paragraph (2), by striking paragraph (1)(B) each place it appears and inserting paragraph (1) , and\n**(C)**\nby adding at the end the following new paragraph:\n(4) Revenue For the purposes of paragraph (1), the revenue from the capital construction fund may include\u2014 (A) income attributable to the operation of any agreement vessel in foreign commerce or domestic trade or fisheries or the operation of a marine terminal in the United States, (B) the net proceeds from the disposition of an agreement vessel or cargo handling equipment or insurance or indemnity attributable to the vessel or cargo handling equipment, (C) the receipts from the investment or reinvestment of amounts held in the fund, and (D) the amount allowable as a deduction under section 167 for the taxable year with respect to the agreement vessels or cargo handling equipment. ,\n**(2)**\nin subsection (b)(2), by striking Amounts in any capital construction fund and all that follows through (not in excess of 60 percent) and inserting An agreed percentage ,\n**(3)**\nin subsection (e)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) In general A qualified withdrawal from the fund is one made in accordance with the terms of the agreement but only if it is for\u2014 (A) the acquisition, construction, repowering, or reconstruction of\u2014 (i) a qualified vessel or a barge or container that is part of the complement of a qualified vessel, or (ii) cargo handling equipment, or (B) the payment of the principal on indebtedness incurred in the acquisition, construction, repowering, or reconstruction of\u2014 (i) a qualified vessel or a barge or container that is part of the complement of a qualified vessel, or (ii) cargo handling equipment. Except to the extent provided in regulations prescribed by the Secretary, subparagraph (A), and so much of subparagraph (B) as relates only to barges and containers, shall apply only with respect to barges and containers constructed in the United States. ,\n**(B)**\nby redesignating paragraph (2) as paragraph (4), and\n**(C)**\nby inserting after paragraph (1) the following:\n(2) Fully automated cargo handling equipment No withdrawals may be made from a capital construction fund to purchase fully automated cargo handling equipment that is remotely operated or remotely monitored with or without the exercise of human intervention or control, if the Secretary determines such equipment would result in a net loss of jobs within a marine terminal. (3) Prohibition on people's republic of china cranes No withdrawals may be made from a capital construction fund to purchase cranes manufactured in the People's Republic of China. ,\n**(4)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (2), by inserting cargo handling equipment, after barge, both places the term appears,\n**(B)**\nin paragraph (3), by inserting cargo handling equipment, after barge, both places the term appears, and\n**(C)**\nin paragraph (4), by inserting cargo handling equipment, after barges, ,\n**(5)**\nin subsection (g)\u2014\n**(A)**\nin the flush matter at the end of paragraph (2), by inserting cargo handling equipment, after advanced , and\n**(B)**\nin paragraph (5)(A)\u2014\n**(i)**\nin the heading, by striking 25 years and inserting 15 years ,\n**(ii)**\nby striking 26th, 27th, 28th, 29th, or 30th taxable year and inserting following specified taxable year , and\n**(iii)**\nby striking the table contained therein and inserting the following:\nIf the amount remains in the fund at the close of the- The applicable percentage is- 16th taxable year 20 percent 17th taxable year 40 percent 18th taxable year 60 percent 19th taxable year 80 percent 20th taxable year 100 percent , and\n**(6)**\nin subsection (i), by striking as in effect on the date of the enactment of this section .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 9. Exemption of student incentive payment agreements from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986, as amended by section 3, is further amended by inserting after section 139J the following new section:\n139K. Student incentive payment agreements In the case of an individual who has entered into an agreement described in section 51509 of title 46, United States Code, gross income does not include any student incentive payments made to such individual pursuant to such agreement. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986, as amended by section 3, is further amended by inserting after the item relating to section 139J the following new item:\nSec. 139K. Student incentive payment agreements. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to payments made after December 31, 2025.\n#### 10. Maritime fuel tax parity\n##### (a) In general\nSection 4041(g) of the Internal Revenue Code of 1986 is amended by adding at the end the following new sentence: For purposes of subsection (a)(2), the exemption under paragraph (1) shall also apply to fuel sold for use or used by a vessel which is both described in section 4042(c)(1) and actually engaged in trade between the Atlantic or Pacific ports of the United States (including any territory or possession of the United States). .\n##### (b) Effective date\nThe amendment made by this section shall apply to fuel sold for use or used after December 31, 2025.\n#### 11. Treatment of maritime prosperity zones as opportunity zones\n##### (a) In general\nSubchapter Z of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n1400Z\u20133. Treatment of maritime prosperity zones as opportunity zones (a) In general A maritime prosperity zone shall be treated as a qualified opportunity zone. (b) Special rules In applying this subchapter to any maritime prosperity zone which is a qualified opportunity zone solely by reason of this section\u2014 (1) In general For purposes of determining\u2014 (A) whether any property which would not be qualified opportunity fund business property without regard to this section is qualified opportunity fund business property, and (B) whether any corporation or partnership which is not a qualified opportunity fund business without regard to this section is a qualified opportunity fund business, section 1400Z\u20132(d) shall be applied with the modifications described in paragraph (2). (2) Modifications The modifications described in this paragraph are as follows: (A) Start date Subparagraphs (B)(i)(I), (C)(i), and (D)(i)(I) of section 1400Z\u20132(d)(2) shall each be applied by substituting the date of the enactment of the Building Ships in America Act of 2025 for December 31, 2017 . (B) Qualified business property Property shall not be treated as qualified opportunity zone business property unless such property is substantially used in an industry which is assigned a code under the North American Industrial Classification System which is described in paragraph (3). (C) Qualified business A trade or business shall not be treated as a qualified opportunity zone business unless such trade or business operates in an industry which is assigned a code under the North American Industrial Classification System which is described in paragraph (3). (3) Eligible north American industrial classification system codes The following codes under the North American Industrial Classification System are the codes described in this paragraph: (A) 48311 (deep sea freight transportation). (B) 483113 (coastal and Great Lakes freight transportation). (C) 483211 (inland water freight transportation). (D) 4883 (support activities for water transportation). (E) 3366 (ship and boat building). (c) Maritime prosperity zone For purposes of this chapter\u2014 (1) In general The term maritime prosperity zone means any population census tract that\u2014 (A) contains or is determined by the Maritime Administrator to be a viable site for\u2014 (i) a shipyard of the United States, (ii) a port, or (iii) a harbor facility, and (B) is designated as a maritime prosperity zone under paragraph (2). (2) Designation A population census tract is designated as a maritime prosperity zone under this paragraph if\u2014 (A) the Maritime Administrator, in consultation with the Secretary of the Navy, nominates the tract for designation as a maritime prosperity zone and notifies the Secretary in writing of such nomination, and (B) the Secretary certifies such nomination and designates such tract as a qualified maritime prosperity zone. (3) Number of population census tracts designated Not more than 100 population census tracts may be designated as maritime prosperity zone. (4) Period for which designation is in effect Except as provided in paragraph (2), a designation as a maritime prosperity zone shall remain in effect for the period\u2014 (A) beginning on the date of the designation, and (B) ending at the close of the 5th calendar year beginning on or after such date of designation. .\n##### (b) Clerical amendment\nThe table of sections for subchapter Z of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 1400Z\u20133. Treatment of maritime prosperity zones as opportunity zones. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act.",
      "versionDate": "",
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
        "actionDate": "2025-05-01",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committees on Transportation and Infrastructure, Ways and Means, Energy and Commerce, Foreign Affairs, Oversight and Government Reform, Education and Workforce, Financial Services, the Judiciary, Natural Resources, Science, Space, and Technology, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3151",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHIPS for America Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-28T20:07:32Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1536is.xml"
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
      "title": "Building Ships in America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Building Ships in America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to support the national defense and economic security of the United States by supporting vessels, ports, and shipyards of the United States and the United States maritime workforce through tax policy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:46Z"
    }
  ]
}
```
