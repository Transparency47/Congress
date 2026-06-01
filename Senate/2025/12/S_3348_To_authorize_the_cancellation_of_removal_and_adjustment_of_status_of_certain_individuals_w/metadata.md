# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3348?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3348
- Title: Dream Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3348
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T16:41:23Z
- Update date including text: 2026-01-07T16:41:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S8509-8512)
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S8509-8512)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3348",
    "number": "3348",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Dream Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:41:23Z",
    "updateDateIncludingText": "2026-01-07T16:41:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S8509-8512)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:06:50Z",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3348is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3348\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Durbin (for himself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize the cancellation of removal and adjustment of status of certain individuals who are long-term United States residents and who entered the United States as children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dream Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) In general**\nExcept as otherwise specifically provided, any term used in this Act that is used in the immigration laws shall have the meaning given such term in the immigration laws.\n**(2) Applicable Federal tax liability**\nThe term applicable Federal tax liability means liability for Federal taxes imposed under the Internal Revenue Code of 1986, including any penalties and interest on Federal taxes imposed under that Code.\n**(3) Armed Forces**\nThe term Armed Forces has the meaning given the term armed forces in section 101 of title 10, United States Code.\n**(4) DACA**\nThe term DACA means deferred action granted to an alien pursuant to the Deferred Action for Childhood Arrivals program announced by President Obama on June 15, 2012.\n**(5) Disability**\nThe term disability has the meaning given such term in section 3(1) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102(1) ).\n**(6) Early childhood education program**\nThe term early childhood education program has the meaning given such term in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 ).\n**(7) Elementary school; high school; secondary school**\nThe terms elementary school , high school , and secondary school have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(8) Immigration laws**\nThe term immigration laws has the meaning given such term in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) ).\n**(9) Institution of higher education**\nThe term institution of higher education \u2014\n**(A)**\nexcept as provided in subparagraph (B), has the meaning given such term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ); and\n**(B)**\ndoes not include an institution of higher education outside of the United States.\n**(10) Permanent resident status on a conditional basis**\nThe term permanent resident status on a conditional basis means status as an alien lawfully admitted for permanent residence on a conditional basis under this Act.\n**(11) Poverty line**\nThe term poverty line has the meaning given such term in section 673 of the Community Services Block Grant Act ( 42 U.S.C. 9902 ).\n**(12) Secretary**\nExcept as otherwise specifically provided, the term Secretary means the Secretary of Homeland Security.\n**(13) Uniformed services**\nThe term Uniformed Services has the meaning given the term uniformed services in section 101(a) of title 10, United States Code.\n#### 3. Permanent resident status on a conditional basis for certain long-term residents who entered the United States as children\n##### (a) Conditional basis for status\nNotwithstanding any other provision of law, an alien shall be considered, at the time of obtaining the status of an alien lawfully admitted for permanent residence under this section, to have obtained such status on a conditional basis subject to the provisions under this Act.\n##### (b) Requirements\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary shall cancel the removal of, and adjust to the status of an alien lawfully admitted for permanent residence on a conditional basis, an alien who is inadmissible or deportable from the United States, is in temporary protected status under section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ), or is the son or daughter of an alien admitted as a nonimmigrant described in subparagraph (E)(i), (E)(ii), (H)(i)(b), or (L) of section 101(a)(15) of such Act ( 8 U.S.C. 1101(a)(15) ) if\u2014\n**(A)**\nthe alien has been continuously physically present in the United States since the date that is 4 years before the date of the enactment of this Act;\n**(B)**\nthe alien was younger than 18 years of age on the date on which the alien initially entered the United States;\n**(C)**\nsubject to paragraphs (2) and (3), the alien\u2014\n**(i)**\nis not inadmissible under paragraph (2), (3), (6)(E), (6)(G), (8), (10)(A), (10)(C), or (10)(D) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) );\n**(ii)**\nhas not ordered, incited, assisted, or otherwise participated in the persecution of any person on account of race, religion, nationality, membership in a particular social group, or political opinion; and\n**(iii)**\nhas not been convicted of\u2014\n**(I)**\nany offense under Federal or State law, other than a State offense for which an essential element is the alien\u2019s immigration status, that is punishable by a maximum term of imprisonment of more than 1 year; or\n**(II)**\n3 or more offenses under Federal or State law, other than State offenses for which an essential element is the alien\u2019s immigration status, for which the alien was convicted on different dates for each of the 3 offenses and imprisoned for an aggregate of 90 days or more;\n**(D)**\nthe alien\u2014\n**(i)**\nhas been admitted to an institution of higher education;\n**(ii)**\nhas earned a high school diploma or a commensurate alternative award from a public or private high school, or has obtained a general education development certificate recognized under State law or a high school equivalency diploma in the United States;\n**(iii)**\nis enrolled in secondary school or in an education program assisting students in\u2014\n**(I)**\nobtaining a regular high school diploma or its recognized equivalent under State law; or\n**(II)**\nin passing a general educational development exam, a high school equivalence diploma examination, or other similar State-authorized exam; or\n**(iv)**\n**(I)**\nhas served, is serving, or has enlisted in the Armed Forces; or\n**(II)**\nin the case of an alien who has been discharged from the Armed Forces, has received an honorable discharge; and\n**(E)**\nthe alien has sworn under penalty of perjury that the alien\u2014\n**(i)**\nhas no unpaid applicable Federal tax liability, which is assessed and is not being disputed;\n**(ii)**\nhas entered into an agreement to resolve any such assessed and undisputed Federal tax liability (via an installment agreement, an offer in compromise, or otherwise) which has been approved by the Commissioner of Internal Revenue; or\n**(iii)**\nhas applied in good faith to enter into an agreement to resolve any such assessed and undisputed Federal tax liability, which has not been rejected by the Commissioner of Internal Revenue.\n**(2) Waiver**\nWith respect to any benefit under this Act, the Secretary may waive the grounds of inadmissibility under paragraph (2), (6)(E), (6)(G), or (10)(D) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) for humanitarian purposes or family unity or if the waiver is otherwise in the public interest.\n**(3) Treatment of expunged convictions**\nAn expunged conviction shall not automatically be treated as an offense under paragraph (1). The Secretary shall evaluate expunged convictions on a case-by-case basis according to the nature and severity of the offense to determine whether, under the particular circumstances, the Secretary determines that the alien should be eligible for cancellation of removal, adjustment to permanent resident status on a conditional basis, or other adjustment of status.\n**(4) DACA recipients**\nThe Secretary shall cancel the removal of, and adjust to the status of an alien lawfully admitted for permanent residence on a conditional basis, an alien who was granted DACA unless the alien has engaged in conduct since the alien was granted DACA that would make the alien ineligible for DACA.\n**(5) Application fee**\n**(A) In general**\nThe Secretary may require an alien applying for permanent resident status on a conditional basis under this section to pay a reasonable fee that is commensurate with the cost of processing the application.\n**(B) Exemption**\nAn applicant may be exempted from paying the fee required under subparagraph (A) if the alien\u2014\n**(i)**\n**(I)**\nis younger than 18 years of age;\n**(II)**\nreceived total income, during the 12-month period immediately preceding the date on which the alien files an application under this section, that is less than 150 percent of the poverty line; and\n**(III)**\nis in foster care or otherwise lacking any parental or other familial support;\n**(ii)**\nis younger than 18 years of age and is homeless;\n**(iii)**\n**(I)**\ncannot care for himself or herself because of a serious, chronic disability; and\n**(II)**\nreceived total income, during the 12-month period immediately preceding the date on which the alien files an application under this section, that is less than 150 percent of the poverty line; or\n**(iv)**\n**(I)**\nduring the 12-month period immediately preceding the date on which the alien files an application under this section, accumulated $10,000 or more in debt as a result of unreimbursed medical expenses incurred by the alien or an immediate family member of the alien; and\n**(II)**\nreceived total income, during the 12-month period immediately preceding the date on which the alien files an application under this section, that is less than 150 percent of the poverty line.\n**(6) Submission of biometric and biographic data**\nThe Secretary may not grant an alien permanent resident status on a conditional basis under this section unless the alien submits biometric and biographic data, in accordance with procedures established by the Secretary. The Secretary shall provide an alternative procedure for aliens who are unable to provide such biometric or biographic data because of a physical impairment.\n**(7) Background checks**\n**(A) Requirement for background checks**\nThe Secretary shall utilize biometric, biographic, and other data that the Secretary determines appropriate\u2014\n**(i)**\nto conduct security and law enforcement background checks of an alien seeking permanent resident status on a conditional basis under this section; and\n**(ii)**\nto determine whether there is any criminal, national security, or other factor that would render the alien ineligible for such status.\n**(B) Completion of background checks**\nThe security and law enforcement background checks of an alien required under subparagraph (A) shall be completed, to the satisfaction of the Secretary, before the date on which the Secretary grants such alien permanent resident status on a conditional basis under this section.\n**(8) Medical examination**\n**(A) Requirement**\nAn alien applying for permanent resident status on a conditional basis under this section shall undergo a medical examination.\n**(B) Policies and procedures**\nThe Secretary, with the concurrence of the Secretary of Health and Human Services, shall prescribe policies and procedures for the nature and timing of the examination required under subparagraph (A).\n**(9) Military selective service**\nAn alien applying for permanent resident status on a conditional basis under this section shall establish that the alien has registered under the Military Selective Service Act ( 50 U.S.C. 3801 et seq. ), if the alien is subject to registration under such Act.\n##### (c) Determination of continuous presence\n**(1) Termination of continuous period**\nAny period of continuous physical presence in the United States of an alien who applies for permanent resident status on a conditional basis under this section shall not terminate when the alien is served a notice to appear under section 239(a) of the Immigration and Nationality Act ( 8 U.S.C. 1229(a) ).\n**(2) Treatment of certain breaks in presence**\n**(A) In general**\nExcept as provided in subparagraphs (B) and (C), an alien shall be considered to have failed to maintain continuous physical presence in the United States under subsection (b)(1)(A) if the alien has departed from the United States for any period exceeding 90 days or for any periods, in the aggregate, exceeding 180 days.\n**(B) Extensions for extenuating circumstances**\nThe Secretary may extend the time periods described in subparagraph (A) for an alien who demonstrates that the failure to timely return to the United States was due to extenuating circumstances beyond the alien\u2019s control, including the serious illness of the alien, or death or serious illness of a parent, grandparent, sibling, or child of the alien.\n**(C) Travel authorized by the secretary**\nAny period of travel outside of the United States by an alien that was authorized by the Secretary may not be counted toward any period of departure from the United States under subparagraph (A).\n##### (d) Limitation on removal of certain aliens\n**(1) In general**\nThe Secretary or the Attorney General may not remove an alien who appears prima facie eligible for relief under this section.\n**(2) Aliens subject to removal**\nThe Secretary shall provide a reasonable opportunity to apply for relief under this section to any alien who requests such an opportunity or who appears prima facie eligible for relief under this section if the alien is in removal proceedings, is the subject of a final removal order, or is the subject of a voluntary departure order.\n**(3) Certain aliens enrolled in elementary or secondary school**\n**(A) Stay of removal**\nThe Attorney General shall stay the removal proceedings of an alien who\u2014\n**(i)**\nmeets all the requirements under subparagraphs (A), (B), and (C) of subsection (b)(1), subject to paragraphs (2) and (3) of such subsection;\n**(ii)**\nis at least 5 years of age; and\n**(iii)**\nis enrolled in an elementary school, a secondary school, or an early childhood education program.\n**(B) Commencement of removal proceedings**\nThe Secretary may not commence removal proceedings for an alien described in subparagraph (A).\n**(C) Employment**\nAn alien whose removal is stayed pursuant to subparagraph (A) or who may not be placed in removal proceedings pursuant to subparagraph (B) shall, upon application to the Secretary, be granted an employment authorization document.\n**(D) Lift of stay**\nThe Secretary or Attorney General may not lift the stay granted to an alien under subparagraph (A) unless the alien ceases to meet the requirements under such subparagraph.\n##### (e) Exemption from numerical limitations\nNothing in this section or in any other law may be construed to apply a numerical limitation on the number of aliens who may be granted permanent resident status on a conditional basis under this Act.\n#### 4. Terms of permanent resident status on a conditional basis\n##### (a) Period of status\nPermanent resident status on a conditional basis is\u2014\n**(1)**\nvalid for a period of 8 years, unless such period is extended by the Secretary; and\n**(2)**\nsubject to termination under subsection (c).\n##### (b) Notice of requirements\nAt the time an alien obtains permanent resident status on a conditional basis, the Secretary shall provide notice to the alien regarding the provisions of this Act and the requirements to have the conditional basis of such status removed.\n##### (c) Termination of status\nThe Secretary may terminate the permanent resident status on a conditional basis of an alien only if the Secretary\u2014\n**(1)**\ndetermines that the alien ceases to meet the requirements under paragraph (1)(C) of section 3(b), subject to paragraphs (2) and (3) of that section; and\n**(2)**\nprior to the termination, provides the alien\u2014\n**(A)**\nnotice of the proposed termination; and\n**(B)**\nthe opportunity for a hearing to provide evidence that the alien meets such requirements or otherwise contest the termination.\n##### (d) Return to previous immigration status\n**(1) In general**\nExcept as provided in paragraph (2), an alien whose permanent resident status on a conditional basis expires under subsection (a)(1) or is terminated under subsection (c) or whose application for such status is denied shall return to the immigration status that the alien had immediately before receiving permanent resident status on a conditional basis or applying for such status, as appropriate.\n**(2) Special rule for temporary protected status**\nAn alien whose permanent resident status on a conditional basis expires under subsection (a)(1) or is terminated under subsection (c) or whose application for such status is denied and who had temporary protected status under section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ) immediately before receiving or applying for such permanent resident status on a conditional basis, as appropriate, may not return to such temporary protected status if\u2014\n**(A)**\nthe relevant designation under section 244(b) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(b) ) has been terminated; or\n**(B)**\nthe Secretary determines that the reason for terminating the permanent resident status on a conditional basis renders the alien ineligible for such temporary protected status.\n#### 5. Removal of conditional basis of permanent resident status\n##### (a) Eligibility for removal of conditional basis\n**(1) In general**\nSubject to paragraph (2), the Secretary shall remove the conditional basis of an alien\u2019s permanent resident status granted under this Act and grant the alien status as an alien lawfully admitted for permanent residence if the alien\u2014\n**(A)**\nis described in paragraph (1)(C) of section 3(b), subject to paragraphs (2) and (3) of that section;\n**(B)**\nhas not abandoned the alien\u2019s residence in the United States; and\n**(C)**\n**(i)**\nhas acquired a degree from an institution of higher education or has completed at least 2 years, in good standing, in a program for a bachelor\u2019s degree or higher degree in the United States;\n**(ii)**\nhas served in the Armed Forces for at least 2 years and, if discharged, received an honorable discharge; or\n**(iii)**\nhas been employed for periods totaling at least 3 years and at least 75 percent of the time that the alien has had a valid employment authorization, except that any period during which the alien is not employed while having a valid employment authorization and is enrolled in an institution of higher education, a secondary school, or an education program described in section 3(b)(1)(D)(iii), shall not count toward the time requirements under this clause.\n**(2) Hardship exception**\nThe Secretary shall remove the conditional basis of an alien\u2019s permanent resident status and grant the alien status as an alien lawfully admitted for permanent residence if the alien\u2014\n**(A)**\nsatisfies the requirements under subparagraphs (A) and (B) of paragraph (1);\n**(B)**\ndemonstrates compelling circumstances for the inability to satisfy the requirements under subparagraph (C) of such paragraph; and\n**(C)**\ndemonstrates that\u2014\n**(i)**\nthe alien has a disability;\n**(ii)**\nthe alien is a full-time caregiver of a minor child; or\n**(iii)**\nthe removal of the alien from the United States would result in extreme hardship to the alien or the alien\u2019s spouse, parent, or child who is a national of the United States or is lawfully admitted for permanent residence.\n**(3) Citizenship requirement**\n**(A) In general**\nExcept as provided in subparagraph (B), the conditional basis of an alien\u2019s permanent resident status granted under this Act may not be removed unless the alien demonstrates that the alien satisfies the requirements under section 312(a) of the Immigration and Nationality Act ( 8 U.S.C. 1423(a) ).\n**(B) Exception**\nSubparagraph (A) shall not apply to an alien who is unable to meet the requirements under such section 312(a) due to disability.\n**(4) Application fee**\n**(A) In general**\nThe Secretary may require aliens applying for lawful permanent resident status under this section to pay a reasonable fee that is commensurate with the cost of processing the application.\n**(B) Exemption**\nAn applicant may be exempted from paying the fee required under subparagraph (A) if the alien\u2014\n**(i)**\n**(I)**\nis younger than 18 years of age;\n**(II)**\nreceived total income, during the 12-month period immediately preceding the date on which the alien files an application under this section, that is less than 150 percent of the poverty line; and\n**(III)**\nis in foster care or otherwise lacking any parental or other familial support;\n**(ii)**\nis younger than 18 years of age and is homeless;\n**(iii)**\n**(I)**\ncannot care for himself or herself because of a serious, chronic disability; and\n**(II)**\nreceived total income, during the 12-month period immediately preceding the date on which the alien files an application under this section, that is less than 150 percent of the poverty line; or\n**(iv)**\n**(I)**\nduring the 12-month period immediately preceding the date on which the alien files an application under this section, the alien accumulated $10,000 or more in debt as a result of unreimbursed medical expenses incurred by the alien or an immediate family member of the alien; and\n**(II)**\nreceived total income, during the 12-month period immediately preceding the date on which the alien files an application under this section, that is less than 150 percent of the poverty line.\n**(5) Submission of biometric and biographic data**\nThe Secretary may not remove the conditional basis of an alien\u2019s permanent resident status unless the alien submits biometric and biographic data, in accordance with procedures established by the Secretary. The Secretary shall provide an alternative procedure for applicants who are unable to provide such biometric data because of a physical impairment.\n**(6) Background checks**\n**(A) Requirement for background checks**\nThe Secretary shall utilize biometric, biographic, and other data that the Secretary determines appropriate\u2014\n**(i)**\nto conduct security and law enforcement background checks of an alien applying for removal of the conditional basis of the alien\u2019s permanent resident status; and\n**(ii)**\nto determine whether there is any criminal, national security, or other factor that would render the alien ineligible for removal of such conditional basis.\n**(B) Completion of background checks**\nThe security and law enforcement background checks of an alien required under subparagraph (A) shall be completed, to the satisfaction of the Secretary, before the date on which the Secretary removes the conditional basis of the alien\u2019s permanent resident status.\n##### (b) Treatment for purposes of naturalization\n**(1) In general**\nFor purposes of title III of the Immigration and Nationality Act ( 8 U.S.C. 1401 et seq. ), an alien granted permanent resident status on a conditional basis shall be considered to have been admitted to the United States, and be present in the United States, as an alien lawfully admitted for permanent residence.\n**(2) Limitation on application for naturalization**\nAn alien may not apply for naturalization while the alien is in permanent resident status on a conditional basis.\n#### 6. Documentation requirements\n##### (a) Documents establishing identity\nAn alien\u2019s application for permanent resident status on a conditional basis may include, as proof of identity\u2014\n**(1)**\na passport or national identity document from the alien\u2019s country of origin that includes the alien\u2019s name and the alien\u2019s photograph or fingerprint;\n**(2)**\nthe alien\u2019s birth certificate and an identity card that includes the alien\u2019s name and photograph;\n**(3)**\na school identification card that includes the alien\u2019s name and photograph, and school records showing the alien\u2019s name and that the alien is or was enrolled at the school;\n**(4)**\na Uniformed Services identification card issued by the Department of Defense;\n**(5)**\nany immigration or other document issued by the United States Government bearing the alien\u2019s name and photograph; or\n**(6)**\na State-issued identification card bearing the alien's name and photograph.\n##### (b) Documents establishing continuous physical presence in the United States\nTo establish that an alien has been continuously physically present in the United States, as required under section 3(b)(1)(A), or to establish that an alien has not abandoned residence in the United States, as required under section 5(a)(1)(B), the alien may submit documents to the Secretary, including\u2014\n**(1)**\nemployment records that include the employer\u2019s name and contact information;\n**(2)**\nrecords from any educational institution the alien has attended in the United States;\n**(3)**\nrecords of service from the Uniformed Services;\n**(4)**\nofficial records from a religious entity confirming the alien\u2019s participation in a religious ceremony;\n**(5)**\npassport entries;\n**(6)**\na birth certificate for a child who was born in the United States;\n**(7)**\nautomobile license receipts or registration;\n**(8)**\ndeeds, mortgages, or rental agreement contracts;\n**(9)**\ntax receipts;\n**(10)**\ninsurance policies;\n**(11)**\nremittance records;\n**(12)**\nrent receipts or utility bills bearing the alien\u2019s name or the name of an immediate family member of the alien, and the alien\u2019s address;\n**(13)**\ncopies of money order receipts for money sent in or out of the United States;\n**(14)**\ndated bank transactions; or\n**(15)**\n2 or more sworn affidavits from individuals who are not related to the alien who have direct knowledge of the alien\u2019s continuous physical presence in the United States, that contain\u2014\n**(A)**\nthe name, address, and telephone number of the affiant; and\n**(B)**\nthe nature and duration of the relationship between the affiant and the alien.\n##### (c) Documents establishing initial entry into the United States\nTo establish under section 3(b)(1)(B) that an alien was younger than 18 years of age on the date on which the alien initially entered the United States, an alien may submit documents to the Secretary, including\u2014\n**(1)**\nan admission stamp on the alien\u2019s passport;\n**(2)**\nrecords from any educational institution the alien has attended in the United States;\n**(3)**\nany document from the Department of Justice or the Department of Homeland Security stating the alien\u2019s date of entry into the United States;\n**(4)**\nhospital or medical records showing medical treatment or hospitalization, the name of the medical facility or physician, and the date of the treatment or hospitalization;\n**(5)**\nrent receipts or utility bills bearing the alien\u2019s name or the name of an immediate family member of the alien, and the alien\u2019s address;\n**(6)**\nemployment records that include the employer\u2019s name and contact information;\n**(7)**\nofficial records from a religious entity confirming the alien\u2019s participation in a religious ceremony;\n**(8)**\na birth certificate for a child who was born in the United States;\n**(9)**\nautomobile license receipts or registration;\n**(10)**\ndeeds, mortgages, or rental agreement contracts;\n**(11)**\ntax receipts;\n**(12)**\ntravel records;\n**(13)**\ncopies of money order receipts sent in or out of the country;\n**(14)**\ndated bank transactions;\n**(15)**\nremittance records; or\n**(16)**\ninsurance policies.\n##### (d) Documents establishing admission to an institution of higher education\nTo establish that an alien has been admitted to an institution of higher education, the alien shall submit to the Secretary a document from the institution of higher education certifying that the alien\u2014\n**(1)**\nhas been admitted to the institution; or\n**(2)**\nis currently enrolled in the institution as a student.\n##### (e) Documents establishing receipt of a degree from an institution of higher education\nTo establish that an alien has acquired a degree from an institution of higher education in the United States, the alien shall submit to the Secretary a diploma or other document from the institution stating that the alien has received such a degree.\n##### (f) Documents establishing receipt of high school diploma, general educational development certificate, or a recognized equivalent\nTo establish that an alien has earned a high school diploma or a commensurate alternative award from a public or private high school, or has obtained a general educational development certificate recognized under State law or a high school equivalency diploma in the United States, the alien shall submit to the Secretary\u2014\n**(1)**\na high school diploma, certificate of completion, or other alternate award;\n**(2)**\na high school equivalency diploma or certificate recognized under State law; or\n**(3)**\nevidence that the alien passed a State-authorized exam, including the general educational development exam, in the United States.\n##### (g) Documents establishing enrollment in an educational program\nTo establish that an alien is enrolled in any school or education program described in section 3(b)(1)(D)(iii), 3(d)(3)(A)(iii), or 5(a)(1)(C), the alien shall submit school records from the United States school that the alien is currently attending that include\u2014\n**(1)**\nthe name of the school; and\n**(2)**\nthe alien\u2019s name, periods of attendance, and current grade or educational level.\n##### (h) Documents establishing exemption from application fees\nTo establish that an alien is exempt from an application fee under section 3(b)(5)(B) or 5(a)(4)(B), the alien shall submit to the Secretary the following relevant documents:\n**(1) Documents to establish age**\nTo establish that an alien meets an age requirement, the alien shall provide proof of identity, as described in subsection (a), that establishes that the alien is younger than 18 years of age.\n**(2) Documents to establish income**\nTo establish the alien\u2019s income, the alien shall provide\u2014\n**(A)**\nemployment records that have been maintained by the Social Security Administration, the Internal Revenue Service, or any other Federal, State, or local government agency;\n**(B)**\nbank records; or\n**(C)**\nat least 2 sworn affidavits from individuals who are not related to the alien and who have direct knowledge of the alien\u2019s work and income that contain\u2014\n**(i)**\nthe name, address, and telephone number of the affiant; and\n**(ii)**\nthe nature and duration of the relationship between the affiant and the alien.\n**(3) Documents to establish foster care, lack of familial support, homelessness, or serious, chronic disability**\nTo establish that the alien was in foster care, lacks parental or familial support, is homeless, or has a serious, chronic disability, the alien shall provide at least 2 sworn affidavits from individuals who are not related to the alien and who have direct knowledge of the circumstances that contain\u2014\n**(A)**\na statement that the alien is in foster care, otherwise lacks any parental or other familiar support, is homeless, or has a serious, chronic disability, as appropriate;\n**(B)**\nthe name, address, and telephone number of the affiant; and\n**(C)**\nthe nature and duration of the relationship between the affiant and the alien.\n**(4) Documents to establish unpaid medical expense**\nTo establish that the alien has debt as a result of unreimbursed medical expenses, the alien shall provide receipts or other documentation from a medical provider that\u2014\n**(A)**\nbear the provider\u2019s name and address;\n**(B)**\nbear the name of the individual receiving treatment; and\n**(C)**\ndocument that the alien has accumulated $10,000 or more in debt in the past 12 months as a result of unreimbursed medical expenses incurred by the alien or an immediate family member of the alien.\n##### (i) Documents establishing qualification for hardship exemption\nTo establish that an alien satisfies one of the criteria for the hardship exemption set forth in section 5(a)(2)(C), the alien shall submit to the Secretary at least 2 sworn affidavits from individuals who are not related to the alien and who have direct knowledge of the circumstances that warrant the exemption, that contain\u2014\n**(1)**\nthe name, address, and telephone number of the affiant; and\n**(2)**\nthe nature and duration of the relationship between the affiant and the alien.\n##### (j) Documents establishing service in the Armed Forces\nTo establish that an alien has served in the Armed Forces for at least 2 years and, if discharged, received an honorable discharge, the alien shall submit to the Secretary official service records showing the character of the alien's service.\n##### (k) Documents establishing employment\n**(1) In general**\nAn alien may satisfy the employment requirement under section 5(a)(1)(C)(iii) by submitting records that\u2014\n**(A)**\nestablish compliance with such employment requirement; and\n**(B)**\nhave been maintained by the Social Security Administration, the Internal Revenue Service, or any other Federal, State, or local government agency.\n**(2) Other documents**\nAn alien who is unable to submit the records described in paragraph (1) may satisfy the employment requirement by submitting at least 2 types of reliable documents that provide evidence of employment, including\u2014\n**(A)**\nbank records;\n**(B)**\nbusiness records;\n**(C)**\nemployer records;\n**(D)**\nrecords of a labor union, day labor center, or organization that assists workers in employment;\n**(E)**\nsworn affidavits from individuals who are not related to the alien and who have direct knowledge of the alien\u2019s work, that contain\u2014\n**(i)**\nthe name, address, and telephone number of the affiant; and\n**(ii)**\nthe nature and duration of the relationship between the affiant and the alien; and\n**(F)**\nremittance records.\n##### (l) Authority To prohibit use of certain documents\nIf the Secretary determines, after publication in the Federal Register and an opportunity for public comment, that any document or class of documents does not reliably establish identity or that permanent resident status on a conditional basis is being obtained fraudulently to an unacceptable degree, the Secretary may prohibit or restrict the use of such document or class of documents.\n#### 7. Rulemaking\n##### (a) Initial publication\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall publish regulations implementing this Act in the Federal Register. Such regulations shall allow eligible individuals to immediately apply affirmatively for the relief available under section 3 without being placed in removal proceedings.\n##### (b) Interim regulations\nNotwithstanding section 553 of title 5, United States Code, the regulations published pursuant to subsection (a) shall be effective, on an interim basis, immediately upon publication in the Federal Register, but may be subject to change and revision after public notice and opportunity for a period of public comment.\n##### (c) Final regulations\nNot later than 180 days after the date on which interim regulations are published under this section, the Secretary shall publish final regulations implementing this Act.\n##### (d) Paperwork Reduction Act\nThe requirements under chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ), shall not apply to any action to implement this Act.\n#### 8. Confidentiality of information\n##### (a) In general\nThe Secretary may not disclose or use information provided in applications filed under this Act or in requests for DACA for the purpose of immigration enforcement.\n##### (b) Referrals prohibited\nThe Secretary may not refer any individual who has been granted permanent resident status on a conditional basis or who was granted DACA to U.S. Immigration and Customs Enforcement, U.S. Customs and Border Protection, or any designee of either such entity.\n##### (c) Limited exception\nNotwithstanding subsections (a) and (b), information provided in an application for permanent resident status on a conditional basis or a request for DACA may be shared with Federal security and law enforcement agencies\u2014\n**(1)**\nfor assistance in the consideration of an application for permanent resident status on a conditional basis;\n**(2)**\nto identify or prevent fraudulent claims;\n**(3)**\nfor national security purposes; or\n**(4)**\nfor the investigation or prosecution of any felony not related to immigration status.\n##### (d) Penalty\nAny person who knowingly uses, publishes, or permits information to be examined in violation of this section shall be fined not more than $10,000.",
      "versionDate": "2025-12-04",
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
        "name": "Immigration",
        "updateDate": "2026-01-07T16:41:23Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3348is.xml"
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
      "title": "Dream Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dream Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the cancellation of removal and adjustment of status of certain individuals who are long-term United States residents and who entered the United States as children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:17Z"
    }
  ]
}
```
