# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/243
- Title: Radiation Exposure Compensation Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 243
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-09-02T19:23:19Z
- Update date including text: 2025-09-02T19:23:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/243",
    "number": "243",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Radiation Exposure Compensation Reauthorization Act",
    "type": "S",
    "updateDate": "2025-09-02T19:23:19Z",
    "updateDateIncludingText": "2025-09-02T19:23:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T16:56:17Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "NM"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MO"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "NM"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "AZ"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ID"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
      "state": "CO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-16",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s243is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 243\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Hawley (for himself, Mr. Luj\u00e1n , Mr. Schmitt , Mr. Heinrich , Mr. Kelly , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo extend the period for filing claims under the Radiation Exposure Compensation Act and to provide for compensation under such Act for claims relating to Manhattan Project waste, and to improve compensation for workers involved in uranium mining.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Radiation Exposure Compensation Reauthorization Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Manhattan Project waste\nSec. 101. Short title.\nSec. 102. Claims relating to Manhattan Project waste.\nSec. 103. Cooperative agreement.\nTITLE II\u2014Compensation for workers involved in uranium mining and individuals living downwind of atmospheric nuclear testing\nSec. 201. Short title.\nSec. 202. References.\nSec. 203. Extension of fund.\nSec. 204. Claims relating to atmospheric testing.\nSec. 205. Claims relating to uranium mining.\nSec. 206. Expansion of use of affidavits in determination of claims; regulations.\nSec. 207. Limitation on claims.\nSec. 208. Grant program on epidemiological impacts of uranium mining and milling.\nSec. 209. Energy Employees Occupational Illness Compensation Program.\nSec. 210. GAO study and report.\nI\nManhattan Project waste\n#### 101. Short title\n##### (a) Short title\nThis title may be cited as the Radiation Exposure Compensation Expansion Act .\n#### 102. Claims relating to Manhattan Project waste\nThe Radiation Exposure Compensation Act ( Public Law 101\u2013426 ; 42 U.S.C. 2210 note) is amended by inserting after section 5 the following:\n5A. Claims relating to Manhattan Project waste (a) In general A claimant shall receive compensation for a claim made under this Act, as described in subsection (b) or (c), if\u2014 (1) a claim for compensation is filed with the Attorney General\u2014 (A) by an individual described in paragraph (2); or (B) on behalf of that individual by an authorized agent of that individual, if the individual is deceased or incapacitated, such as\u2014 (i) an executor of estate of that individual; or (ii) a legal guardian or conservator of that individual; (2) that individual, or if applicable, an authorized agent of that individual, demonstrates that the individual\u2014 (A) was physically present in an affected area for a period of at least 2 years after January 1, 1949; and (B) contracted a specified disease after such period of physical presence; (3) the Attorney General certifies that the identity of that individual, and if applicable, the authorized agent of that individual, is not fraudulent or otherwise misrepresented; and (4) the Attorney General determines that the claimant has satisfied the applicable requirements of this Act. (b) Losses available to living affected individuals (1) In general In the event of a claim qualifying for compensation under subsection (a) that is submitted to the Attorney General to be eligible for compensation under this section at a time when the individual described in subsection (a)(2) is living, the amount of compensation under this section shall be in an amount that is the greater of $50,000 or the total amount of compensation for which the individual is eligible under paragraph (2). (2) Losses due to medical expenses A claimant described in paragraph (1) shall be eligible to receive, upon submission of contemporaneous written medical records, reports, or billing statements created by or at the direction of a licensed medical professional who provided contemporaneous medical care to the claimant, additional compensation in the amount of all documented out-of-pocket medical expenses incurred as a result of the specified disease suffered by that claimant, such as any medical expenses not covered, paid for, or reimbursed through\u2014 (A) any public or private health insurance; (B) any employee health insurance; (C) any workers\u2019 compensation program; or (D) any other public, private, or employee health program or benefit. (c) Payments to beneficiaries of deceased individuals In the event that an individual described in subsection (a)(2) who qualifies for compensation under subsection (a) is deceased at the time of submission of the claim\u2014 (1) a surviving spouse may, upon submission of a claim and records sufficient to satisfy the requirements of subsection (a) with respect to the deceased individual, receive compensation in the amount of $25,000; or (2) in the event that there is no surviving spouse, the surviving children, minor or otherwise, of the deceased individual may, upon submission of a claim and records sufficient to satisfy the requirements of subsection (a) with respect to the deceased individual, receive compensation in the total amount of $25,000, paid in equal shares to each surviving child. (d) Affected area For purposes of this section, the term affected area means\u2014 (1) in the State of Missouri, the ZIP Codes of 63031, 63033, 63034, 63042, 63045, 63074, 63114, 63135, 63138, 63044, 63121, 63140, 63145, 63147, 63102, 63304, 63134, 63043, 63341, 63368, and 63367; (2) in the State of Tennessee, the ZIP Codes of 37716, 37840, 37719, 37748, 37763, 37828, 37769, 37710, 37845, 37887, 37829, 37854, 37830, and 37831; (3) in the State of Alaska, the ZIP Codes of 99546 and 99547; and (4) in the State of Kentucky, the ZIP Codes of 42001, 42003, and 42086. (e) Specified disease For purposes of this section, the term specified disease means any of the following: (1) Any leukemia, other than chronic lymphocytic leukemia, provided that the initial exposure occurred after the age of 20 and the onset of the disease was at least 2 years after first exposure. (2) Any of the following diseases, provided that the onset was at least 2 years after the initial exposure: (A) Multiple myeloma. (B) Lymphoma, other than Hodgkin\u2019s disease. (C) Primary cancer of the\u2014 (i) thyroid; (ii) male or female breast; (iii) esophagus; (iv) stomach; (v) pharynx; (vi) small intestine; (vii) pancreas; (viii) bile ducts; (ix) gall bladder; (x) salivary gland; (xi) urinary bladder; (xii) brain; (xiii) colon; (xiv) ovary; (xv) bone; (xvi) renal; (xvii) liver, except if cirrhosis or hepatitis B is indicated; or (xviii) lung. (f) Physical presence (1) In general For purposes of this section, the Attorney General shall not determine that a claimant has satisfied the requirements of subsection (a) unless demonstrated by submission of\u2014 (A) contemporaneous written residential documentation and at least 1 additional employer-issued or government-issued document or record that the claimant, for at least 2 years after January 1, 1949, was physically present in an affected area; or (B) other documentation determined by the Attorney General to demonstrate that the claimant, for at least 2 years after January 1, 1949, was physically present in an affected area. (2) Types of physical presence For purposes of determining physical presence under this section, a claimant shall be considered to have been physically present in an affected area if\u2014 (A) the claimant\u2019s primary residence was in the affected area; (B) the claimant\u2019s place of employment was in the affected area; or (C) the claimant attended school in the affected area. (g) Disease contraction in affected areas For purposes of this section, the Attorney General shall not determine that a claimant has satisfied the requirements of subsection (a) unless the claimant submits\u2014 (1) written medical records or reports created by or at the direction of a licensed medical professional, created contemporaneously with the provision of medical care to the claimant, that the claimant, after a period of physical presence in an affected area, contracted a specified disease; or (2) other documentation determined by the Attorney General to demonstrate that the claimant contracted a specified disease after a period of physical presence in an affected area. .\n#### 103. Cooperative agreement\n##### (a) In general\nNot later than September 30, 2025, the Secretary of Energy, acting through the Director of the Office of Legacy Management, shall award to an eligible association a cooperative agreement to support the safeguarding of human and ecological health at the Amchitka, Alaska, Site.\n##### (b) Requirements\nA cooperative agreement awarded under subsection (a)\u2014\n**(1)**\nmay be used to fund\u2014\n**(A)**\nresearch and development that will improve and focus long-term surveillance and monitoring of the site;\n**(B)**\nworkforce development at the site; and\n**(C)**\nsuch other activities as the Secretary considers appropriate; and\n**(2)**\nshall require that the eligible association\u2014\n**(A)**\nengage in stakeholder engagement; and\n**(B)**\nto the greatest extent practicable, incorporate Indigenous knowledge and the participation of local Indian Tribes in research and development and workforce development activities.\n##### (c) Definitions\nIn this section:\n**(1) Eligible association**\nThe term eligible association means an association of 2 or more of the following:\n**(A)**\nAn institution of higher education (as that term is defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) located in the State of Alaska.\n**(B)**\nAn agency of the State of Alaska.\n**(C)**\nA local Indian Tribe.\n**(D)**\nAn organization\u2014\n**(i)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code; and\n**(ii)**\nlocated in the State of Alaska.\n**(2) Local indian tribe**\nThe term local Indian Tribe means an Indian tribe (as that term is defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) that is located in the Aleut Region of the State of Alaska.\nII\nCompensation for workers involved in uranium mining and individuals living downwind of atmospheric nuclear testing\n#### 201. Short title\nThis title may be cited as the Radiation Exposure Compensation Act Amendments of 2025 .\n#### 202. References\nExcept as otherwise specifically provided, whenever in this title an amendment or repeal is expressed in terms of an amendment to or repeal of a section or other provision of law, the reference shall be considered to be made to a section or other provision of the Radiation Exposure Compensation Act ( Public Law 101\u2013426 ; 42 U.S.C. 2210 note).\n#### 203. Extension of fund\nSection 3(d) is amended\u2014\n**(1)**\nby striking the first sentence and inserting The Fund shall terminate 6 years after the date of the enactment of the Radiation Exposure Compensation Act Amendments of 2025 . ; and\n**(2)**\nby striking 2-year and inserting 6-year .\n#### 204. Claims relating to atmospheric testing\n##### (a) Leukemia claims relating to Trinity Test in New Mexico and tests at the Nevada site and in the Pacific\nSection 4(a)(1)(A) is amended\u2014\n**(1)**\nin clause (i)\u2014\n**(A)**\nin subclause (I), by striking October 31, 1958 and inserting November 6, 1962 ;\n**(B)**\nin subclause (II)\u2014\n**(i)**\nby striking in the affected area and inserting in an affected area ; and\n**(ii)**\nby striking or after the semicolon;\n**(C)**\nby redesignating subclause (III) as subclause (V); and\n**(D)**\nby inserting after subclause (II) the following:\n(III) was physically present in an affected area for a period of at least 1 year during the period beginning on September 24, 1944, and ending on November 6, 1962; (IV) was physically present in an affected area\u2014 (aa) for a period of at least 1 year during the period beginning on July 1, 1946, and ending on November 6, 1962; or (bb) for the period beginning on April 25, 1962, and ending on November 6, 1962; or ; and\n**(2)**\nin clause (ii)(I), by striking physical presence described in subclause (I) or (II) of clause (i) or onsite participation described in clause (i)(III) and inserting physical presence described in subclause (I), (II), (III), or (IV) of clause (i) or onsite participation described in clause (i)(V) .\n##### (b) Amounts for claims related to leukemia\nSection 4(a)(1) is amended\u2014\n**(1)**\nin subparagraph (A), by striking an amount and inserting the amount ; and\n**(2)**\nby striking subparagraph (B) and inserting the following:\n(B) Amount If the conditions described in subparagraph (C) are met, an individual who is described in subparagraph (A) shall receive $100,000. .\n##### (c) Conditions for claims related to leukemia\nSection 4(a)(1)(C) is amended\u2014\n**(1)**\nby striking clause (i); and\n**(2)**\nby redesignating clauses (ii) and (iii) as clauses (i) and (ii), respectively.\n##### (d) Specified diseases claims relating to Trinity Test in New Mexico and tests at the Nevada site and in the Pacific\nSection 4(a)(2) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking in the affected area and inserting in an affected area ;\n**(B)**\nby striking 2 years and inserting 1 year ; and\n**(C)**\nby striking October 31, 1958 and inserting November 6, 1962 ;\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby striking in the affected area and inserting in an affected area ; and\n**(B)**\nby striking or at the end;\n**(3)**\nby redesignating subparagraph (C) as subparagraph (E); and\n**(4)**\nby inserting after subparagraph (B) the following:\n(C) was physically present in an affected area for a period of at least 1 year during the period beginning on September 24, 1944, and ending on November 6, 1962; (D) was physically present in an affected area\u2014 (i) for a period of at least 1 year during the period beginning on July 1, 1946, and ending on November 6, 1962; or (ii) for the period beginning on April 25, 1962, and ending on November 6, 1962; or .\n##### (e) Amounts for claims related to specified diseases\nSection 4(a)(2) is amended in the matter following subparagraph (E) (as redesignated by subsection (d) of this section) by striking $50,000 (in the case of an individual described in subparagraph (A) or (B)) or $75,000 (in the case of an individual described in subparagraph (C)), and inserting $100,000 .\n##### (f) Downwind States\nSection 4(b)(1) is amended to read as follows:\n(1) affected area means\u2014 (A) except as provided under subparagraphs (B) and (C), Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, and Guam; (B) with respect to a claim by an individual under subsection (a)(1)(A)(i)(III) or subsection (a)(2)(C), only New Mexico; and (C) with respect to a claim by an individual under subsection (a)(1)(A)(i)(IV) or subsection (a)(2)(D), only Guam. .\n##### (g) Chronic lymphocytic leukemia as a specified disease\nSection 4(b)(2) is amended by striking other than chronic lymphocytic leukemia and inserting including chronic lymphocytic leukemia .\n#### 205. Claims relating to uranium mining\n##### (a) Employees of mines and mills\nSection 5(a)(1)(A)(i) is amended\u2014\n**(1)**\nby inserting (I) after (i) ;\n**(2)**\nby striking December 31, 1971; and and inserting December 31, 1990; or ; and\n**(3)**\nby adding at the end the following:\n(II) was employed as a core driller in a State referred to in subclause (I) during the period described in such subclause; and .\n##### (b) Miners\nSection 5(a)(1)(A)(ii)(I) is amended by inserting or renal cancer or any other chronic renal disease, including nephritis and kidney tubal tissue injury after nonmalignant respiratory disease .\n##### (c) Millers, core drillers, and ore transporters\nSection 5(a)(1)(A)(ii)(II) is amended\u2014\n**(1)**\nby inserting , core driller, after was a miller ;\n**(2)**\nby inserting , or was involved in remediation efforts at such a uranium mine or uranium mill, after ore transporter ;\n**(3)**\nby inserting (I) after clause (i) ; and\n**(4)**\nby striking all that follows nonmalignant respiratory disease and inserting or renal cancer or any other chronic renal disease, including nephritis and kidney tubal tissue injury; or .\n##### (d) Combined work histories\nSection 5(a)(1)(A)(ii) is further amended\u2014\n**(1)**\nby striking or at the end of subclause (I); and\n**(2)**\nby adding at the end the following:\n(III) (aa) does not meet the conditions of subclause (I) or (II); (bb) worked, during the period described in clause (i)(I), in two or more of the following positions: miner, miller, core driller, and ore transporter; (cc) meets the requirements of paragraph (4) or (5), or both; and (dd) submits written medical documentation that the individual developed lung cancer or a nonmalignant respiratory disease or renal cancer or any other chronic renal disease, including nephritis and kidney tubal tissue injury after exposure to radiation through work in one or more of the positions referred to in item (bb); .\n##### (e) Dates of operation of uranium mine\nSection 5(a)(2)(A) is amended by striking December 31, 1971 and inserting December 31, 1990 .\n##### (f) Special rules relating to combined work histories\nSection 5(a) is amended by adding at the end the following:\n(4) Special rule relating to combined work histories for individuals with at least one year of experience An individual meets the requirements of this paragraph if the individual worked in one or more of the positions referred to in paragraph (1)(A)(ii)(III)(bb) for a period of at least one year during the period described in paragraph (1)(A)(i)(I). (5) Special rule relating to combined work histories for miners An individual meets the requirements of this paragraph if the individual, during the period described in paragraph (1)(A)(i)(I), worked as a miner and was exposed to such number of working level months that the Attorney General determines, when combined with the exposure of such individual to radiation through work as a miller, core driller, or ore transporter during the period described in paragraph (1)(A)(i)(I), results in such individual being exposed to a total level of radiation that is greater or equal to the level of exposure of an individual described in paragraph (4) . .\n##### (g) Definition of Core driller\nSection 5(b) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (7);\n**(2)**\nby striking the period at the end of paragraph (8) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(9) the term core driller means any individual employed to engage in the act or process of obtaining cylindrical rock samples of uranium or vanadium by means of a borehole drilling machine for the purpose of mining uranium or vanadium. .\n#### 206. Expansion of use of affidavits in determination of claims; regulations\n##### (a) Affidavits\nSection 6(b) is amended by adding at the end the following:\n(3) Affidavits (A) Employment History For purposes of this Act, the Attorney General shall accept a written affidavit or declaration as evidence to substantiate the employment history of an individual as a miner, miller, core driller, or ore transporter if the affidavit\u2014 (i) is provided in addition to other material that may be used to substantiate the employment history of the individual; (ii) attests to the employment history of the individual; (iii) is made subject to penalty for perjury; and (iv) is made by a person other than the individual filing the claim. (B) Physical Presence in Affected Area For purposes of this Act, the Attorney General shall accept a written affidavit or declaration as evidence to substantiate an individual\u2019s physical presence in an affected area (as defined in section 4(b)(1)) during a period described in section 4(a)(1)(A)(i) or section 4(a)(2) if the affidavit\u2014 (i) is provided in addition to other material that may be used to substantiate the individual\u2019s presence in an affected area during that time period; (ii) attests to the individual\u2019s presence in an affected area during that period; (iii) is made subject to penalty for perjury; and (iv) is made by a person other than the individual filing the claim. (C) Participation at Testing Site For purposes of this Act, the Attorney General shall accept a written affidavit or declaration as evidence to substantiate an individual\u2019s participation onsite in a test involving the atmospheric detonation of a nuclear device if the affidavit\u2014 (i) is provided in addition to other material that may be used to substantiate the individual\u2019s participation onsite in a test involving the atmospheric detonation of a nuclear device; (ii) attests to the individual\u2019s participation onsite in a test involving the atmospheric detonation of a nuclear device; (iii) is made subject to penalty for perjury; and (iv) is made by a person other than the individual filing the claim. .\n##### (b) Technical and conforming amendments\nSection 6 is amended\u2014\n**(1)**\nin subsection (b)(2)(C), by striking section 4(a)(2)(C) and inserting section 4(a)(2)(E) ;\n**(2)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking subsection (a)(1), (a)(2)(A), or (a)(2)(B) of section 4 and inserting subsection (a)(1), (a)(2)(A), (a)(2)(B), (a)(2)(C), or (a)(2)(D) of section 4 ; and\n**(ii)**\nin clause (i), by striking subsection (a)(1), (a)(2)(A), or (a)(2)(B) of section 4 and inserting subsection (a)(1), (a)(2)(A), (a)(2)(B), (a)(2)(C), or (a)(2)(D) of section 4 ; and\n**(B)**\nin subparagraph (B), by striking section 4(a)(2)(C) and inserting section 4(a)(2)(E) ; and\n**(3)**\nin subsection (e), by striking subsection (a)(1), (a)(2)(A), or (a)(2)(B) of section 4 and inserting subsection (a)(1), (a)(2)(A), (a)(2)(B), (a)(2)(C), or (a)(2)(D) of section 4 .\n##### (c) Regulations\n**(1) In general**\nSection 6(k) is amended by adding at the end the following: Not later than 180 days after the date of enactment of the Radiation Exposure Compensation Act Amendments of 2025 , the Attorney General shall issue revised regulations to carry out this Act. .\n**(2) Considerations in revisions**\nIn issuing revised regulations under section 6(k) of the Radiation Exposure Compensation Act ( Public Law 101\u2013426 ; 42 U.S.C. 2210 note), as amended under paragraph (1), the Attorney General shall ensure that procedures with respect to the submission and processing of claims under such Act take into account and make allowances for the law, tradition, and customs of Indian tribes, including by accepting as a record of proof of physical presence for a claimant a grazing permit, a homesite lease, a record of being a holder of a post office box, a letter from an elected leader of an Indian tribe, or a record of any recognized tribal association or organization.\n#### 207. Limitation on claims\n##### (a) Extension of filing time\nSection 8(a) is amended\u2014\n**(1)**\nby striking 2 years and inserting 5 years ; and\n**(2)**\nby striking RECA Extension Act of 2022 and inserting Radiation Exposure Compensation Act Amendments of 2025 .\n##### (b) Resubmittal of claims\nSection 8(b) is amended to read as follows:\n(b) Resubmittal of claims (1) Denied claims After the date of enactment of the Radiation Exposure Compensation Act Amendments of 2025 , any claimant who has been denied compensation under this Act may resubmit a claim for consideration by the Attorney General in accordance with this Act not more than three times. Any resubmittal made before the date of the enactment of the Radiation Exposure Compensation Act Amendments of 2025 shall not be applied to the limitation under the preceding sentence. (2) Previously successful claims (A) In general After the date of enactment of the Radiation Exposure Compensation Act Amendments of 2025 , any claimant who received compensation under this Act may submit a request to the Attorney General for additional compensation and benefits. Such request shall contain\u2014 (i) the claimant\u2019s name, social security number, and date of birth; (ii) the amount of award received under this Act before the date of enactment of the Radiation Exposure Compensation Act Amendments of 2025 ; (iii) any additional benefits and compensation sought through such request; and (iv) any additional information required by the Attorney General. (B) Additional Compensation If the claimant received compensation under this Act before the date of enactment of the Radiation Exposure Compensation Act Amendments of 2025 and submits a request under subparagraph (A) , the Attorney General shall\u2014 (i) pay the claimant the amount that is equal to any excess of\u2014 (I) the amount the claimant is eligible to receive under this Act (as amended by the Radiation Exposure Compensation Act Amendments of 2025 ); minus (II) the aggregate amount paid to the claimant under this Act before the date of enactment of the Radiation Exposure Compensation Act Amendments of 2025 ; and (ii) in any case in which the claimant was compensated under section 4, provide the claimant with medical benefits under section 4(a)(5). .\n#### 208. Grant program on epidemiological impacts of uranium mining and milling\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term institution of higher education has the meaning given under section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 );\n**(2)**\nthe term program means the grant program established under subsection (b); and\n**(3)**\nthe term Secretary means the Secretary of Health and Human Services.\n##### (b) Establishment\nThe Secretary shall establish a grant program relating to the epidemiological impacts of uranium mining and milling. Grants awarded under the program shall be used for the study of the epidemiological impacts of uranium mining and milling among non-occupationally exposed individuals, including family members of uranium miners and millers.\n##### (c) Administration\nThe Secretary shall administer the program through the National Institute of Environmental Health Sciences.\n##### (d) Eligibility and application\nAny institution of higher education or nonprofit private entity shall be eligible to apply for a grant. To apply for a grant an eligible institution or entity shall submit to the Secretary an application at such time, in such manner, and containing or accompanied by such information as the Secretary may reasonably require.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $3,000,000 for each of fiscal years 2025 through 2027.\n#### 209. Energy Employees Occupational Illness Compensation Program\n##### (a) Covered employees with cancer\nSection 3621(9) of the Energy Employees Occupational Illness Compensation Program Act of 2000 ( 42 U.S.C. 7384l(9) ) is amended by striking subparagraph (A) and inserting the following:\n(A) An individual with a specified cancer who is a member of the Special Exposure Cohort, if and only if\u2014 (i) that individual contracted that specified cancer after beginning employment at a Department of Energy facility (in the case of a Department of Energy employee or Department of Energy contractor employee) or at an atomic weapons employer facility (in the case of an atomic weapons employee); or (ii) that individual\u2014 (I) contracted that specified cancer after beginning employment in a uranium mine or uranium mill described under section 5(a)(1)(A)(i) of the Radiation Exposure Compensation Act ( 42 U.S.C. 2210 note) (including any individual who was employed in core drilling or the transport of uranium ore or vanadium-uranium ore from such mine or mill) located in Colorado, New Mexico, Arizona, Wyoming, South Dakota, Washington, Utah, Idaho, North Dakota, Oregon, Texas, or any State the Attorney General makes a determination under section 5(a)(2) of that Act for inclusion of eligibility under section 5(a)(1) of that Act; and (II) was employed in a uranium mine or uranium mill described under subclause (I) (including any individual who was employed in core drilling or the transport of uranium ore or vanadium-uranium ore from such mine or mill) at any time during the period beginning on January 1, 1942, and ending on December 31, 1990. .\n##### (b) Members of Special Exposure Cohort\nSection 3626 of the Energy Employees Occupational Illness Compensation Program Act of 2000 ( 42 U.S.C. 7384q ) is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (1) and inserting the following:\n(1) The Advisory Board on Radiation and Worker Health under section 3624 shall advise the President whether there is a class of employees\u2014 (A) at any Department of Energy facility who likely were exposed to radiation at that facility but for whom it is not feasible to estimate with sufficient accuracy the radiation dose they received; and (B) employed in a uranium mine or uranium mill described under section 5(a)(1)(A)(i) of the Radiation Exposure Compensation Act ( 42 U.S.C. 2210 note) (including any individual who was employed in core drilling or the transport of uranium ore or vanadium-uranium ore from such mine or mill) located in Colorado, New Mexico, Arizona, Wyoming, South Dakota, Washington, Utah, Idaho, North Dakota, Oregon, Texas, and any State the Attorney General makes a determination under section 5(a)(2) of that Act for inclusion of eligibility under section 5(a)(1) of that Act, at any time during the period beginning on January 1, 1942, and ending on December 31, 1990, who likely were exposed to radiation at that mine or mill but for whom it is not feasible to estimate with sufficient accuracy the radiation dose they received. ; and\n**(2)**\nby striking subsection (b) and inserting the following:\n(b) Designation of additional members (1) Subject to the provisions of section 3621(14)(C), the members of a class of employees at a Department of Energy facility, or at an atomic weapons employer facility, may be treated as members of the Special Exposure Cohort for purposes of the compensation program if the President, upon recommendation of the Advisory Board on Radiation and Worker Health, determines that\u2014 (A) it is not feasible to estimate with sufficient accuracy the radiation dose that the class received; and (B) there is a reasonable likelihood that such radiation dose may have endangered the health of members of the class. (2) Subject to the provisions of section 3621(14)(C), the members of a class of employees employed in a uranium mine or uranium mill described under section 5(a)(1)(A)(i) of the Radiation Exposure Compensation Act ( 42 U.S.C. 2210 note) (including any individual who was employed in core drilling or the transport of uranium ore or vanadium-uranium ore from such mine or mill) located in Colorado, New Mexico, Arizona, Wyoming, South Dakota, Washington, Utah, Idaho, North Dakota, Oregon, Texas, and any State the Attorney General makes a determination under section 5(a)(2) of that Act for inclusion of eligibility under section 5(a)(1) of that Act, at any time during the period beginning on January 1, 1942, and ending on December 31, 1990, may be treated as members of the Special Exposure Cohort for purposes of the compensation program if the President, upon recommendation of the Advisory Board on Radiation and Worker Health, determines that\u2014 (A) it is not feasible to estimate with sufficient accuracy the radiation dose that the class received; and (B) there is a reasonable likelihood that such radiation dose may have endangered the health of members of the class. .\n#### 210. GAO study and report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall conduct, and submit to Congress a report describing the results of, a study on the importance of, and need for, unmet medical benefits coverage for individuals who were exposed to radiation in atmospheric nuclear tests conducted by the Federal Government, and recommendations to provide such unmet medical benefits coverage for such individuals.",
      "versionDate": "2025-01-24",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Arizona",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Cancer",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Digestive and metabolic diseases",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-19T19:36:35Z"
          },
          {
            "name": "Government liability",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Guam",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "North Dakota",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Nuclear weapons",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Radiation",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "South Dakota",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "U.S. territories and protectorates",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Washington State",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Worker safety and health",
            "updateDate": "2025-03-19T19:36:36Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-03-19T19:36:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-01T14:18:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s243",
          "measure-number": "243",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-09-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s243v00",
            "update-date": "2025-09-02"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<div><strong>Radiation Exposure Compensation Reauthorization Act</strong></div><div>\u00a0</div><p>This bill reauthorizes and expands programs that compensate individuals who were exposed to radiation during certain nuclear testing or uranium mining and who subsequently developed medical conditions, including cancers.</p><p>Under current law, compensation is payable to individuals based on requirements including the (1) dates when exposure occurred, (2) duration of exposure, (3) type of exposure, and (4) resulting medical condition.\u00a0</p><p>Among other changes to this program, the bill (1) extends the eligible dates when qualifying atmospheric exposure occurred, (2) authorizes compensation to individuals with combined work histories in uranium mining,\u00a0(3)\u00a0adds core drilling as an eligible mining occupation, and (4) increases the amount of compensation awarded\u00a0to qualifying individuals.\u00a0</p><p>The bill also expands this program to compensate individuals\u00a0located in specified areas in Alaska, Kentucky, Missouri, and Tennessee\u00a0associated with waste from the Manhattan Project and who subsequently developed specified types of cancer.</p><p>The bill extends until five years after this bill's enactment the statute of limitations for the filing of claims.\u00a0</p><p>The bill also expands eligibility under an existing occupational illness compensation program for former Department of Energy employees.</p><p>The bill also establishes a grant program for institutions of higher education to study the epidemiological impacts of uranium mining and milling among individuals without occupational exposure.</p><p>The bill directs the Government Accountability Office to study and report to Congress on the unmet medical benefits coverage for individuals who were exposed to radiation in atmospheric nuclear tests conducted by the federal government.</p>"
        },
        "title": "Radiation Exposure Compensation Reauthorization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s243.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<div><strong>Radiation Exposure Compensation Reauthorization Act</strong></div><div>\u00a0</div><p>This bill reauthorizes and expands programs that compensate individuals who were exposed to radiation during certain nuclear testing or uranium mining and who subsequently developed medical conditions, including cancers.</p><p>Under current law, compensation is payable to individuals based on requirements including the (1) dates when exposure occurred, (2) duration of exposure, (3) type of exposure, and (4) resulting medical condition.\u00a0</p><p>Among other changes to this program, the bill (1) extends the eligible dates when qualifying atmospheric exposure occurred, (2) authorizes compensation to individuals with combined work histories in uranium mining,\u00a0(3)\u00a0adds core drilling as an eligible mining occupation, and (4) increases the amount of compensation awarded\u00a0to qualifying individuals.\u00a0</p><p>The bill also expands this program to compensate individuals\u00a0located in specified areas in Alaska, Kentucky, Missouri, and Tennessee\u00a0associated with waste from the Manhattan Project and who subsequently developed specified types of cancer.</p><p>The bill extends until five years after this bill's enactment the statute of limitations for the filing of claims.\u00a0</p><p>The bill also expands eligibility under an existing occupational illness compensation program for former Department of Energy employees.</p><p>The bill also establishes a grant program for institutions of higher education to study the epidemiological impacts of uranium mining and milling among individuals without occupational exposure.</p><p>The bill directs the Government Accountability Office to study and report to Congress on the unmet medical benefits coverage for individuals who were exposed to radiation in atmospheric nuclear tests conducted by the federal government.</p>",
      "updateDate": "2025-09-02",
      "versionCode": "id119s243"
    },
    "title": "Radiation Exposure Compensation Reauthorization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<div><strong>Radiation Exposure Compensation Reauthorization Act</strong></div><div>\u00a0</div><p>This bill reauthorizes and expands programs that compensate individuals who were exposed to radiation during certain nuclear testing or uranium mining and who subsequently developed medical conditions, including cancers.</p><p>Under current law, compensation is payable to individuals based on requirements including the (1) dates when exposure occurred, (2) duration of exposure, (3) type of exposure, and (4) resulting medical condition.\u00a0</p><p>Among other changes to this program, the bill (1) extends the eligible dates when qualifying atmospheric exposure occurred, (2) authorizes compensation to individuals with combined work histories in uranium mining,\u00a0(3)\u00a0adds core drilling as an eligible mining occupation, and (4) increases the amount of compensation awarded\u00a0to qualifying individuals.\u00a0</p><p>The bill also expands this program to compensate individuals\u00a0located in specified areas in Alaska, Kentucky, Missouri, and Tennessee\u00a0associated with waste from the Manhattan Project and who subsequently developed specified types of cancer.</p><p>The bill extends until five years after this bill's enactment the statute of limitations for the filing of claims.\u00a0</p><p>The bill also expands eligibility under an existing occupational illness compensation program for former Department of Energy employees.</p><p>The bill also establishes a grant program for institutions of higher education to study the epidemiological impacts of uranium mining and milling among individuals without occupational exposure.</p><p>The bill directs the Government Accountability Office to study and report to Congress on the unmet medical benefits coverage for individuals who were exposed to radiation in atmospheric nuclear tests conducted by the federal government.</p>",
      "updateDate": "2025-09-02",
      "versionCode": "id119s243"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s243is.xml"
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
      "title": "Radiation Exposure Compensation Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Radiation Exposure Compensation Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Radiation Exposure Compensation Act Amendments of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Radiation Exposure Compensation Expansion Act",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend the period for filing claims under the Radiation Exposure Compensation Act and to provide for compensation under such Act for claims relating to Manhattan Project waste, and to improve compensation for workers involved in uranium mining.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:35Z"
    }
  ]
}
```
