# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2231
- Title: GLOBE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2231
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2026-01-10T06:41:08Z
- Update date including text: 2026-01-10T06:41:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2231",
    "number": "2231",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "GLOBE Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T06:41:08Z",
    "updateDateIncludingText": "2026-01-10T06:41:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-09",
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
          "date": "2025-07-09T22:21:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "VA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "HI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "DE"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "WA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "RI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "WI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NV"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-09",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NJ"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "MD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2231is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2231\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Markey (for himself, Mr. Kaine , Mr. Schatz , Mr. Coons , Mr. Padilla , Mr. Schiff , Mrs. Murray , Mr. Whitehouse , Mr. Murphy , Ms. Baldwin , Ms. Cortez Masto , Ms. Hirono , Mr. Merkley , Mr. Sanders , Mr. Welch , Mr. Booker , Mr. Wyden , Ms. Rosen , Mrs. Shaheen , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo protect human rights and enhance opportunities for LGBTQI people around the world, and for other purposes.\n#### 1. Short titles; table of contents\n##### (a) Short titles\nThis Act may be cited as the Greater Leadership Overseas for the Benefit of Equality Act of 2025 or the GLOBE Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short titles; table of contents.\nSec. 2. Findings.\nSec. 3. Definitions.\nSec. 4. Documenting and responding to bias-motivated violence against LGBTQI people abroad.\nSec. 5. Sanctions on individuals responsible for violations of human rights against LGBTQI people.\nSec. 6. Combating international criminalization of LGBTQI status, expression, or conduct.\nSec. 7. Foreign assistance to protect human rights of LGBTQI people.\nSec. 8. Global health inclusivity.\nSec. 9. Immigration reform.\nSec. 10. Issuance of passports and guarantee of citizenship to certain children born abroad.\nSec. 11. Engaging international organizations in the fight against LGBTQI discrimination.\nSec. 12. Representing the rights of United States LGBTQI citizens deployed to diplomatic and consular posts.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States has been and must always be the global leader in protecting human rights, including the rights of lesbian, gay, bisexual, transgender, queer, and intersex (LGBTQI) peoples around the world.\n**(2)**\nThe norms of good governance, human rights protections, and the rule of law have been violated unconscionably with respect to LGBTQI peoples in an overwhelming majority of countries around the world, where LGBTQI people face violence, hatred, bigotry, and discrimination because of who they are and whom they love.\n**(3)**\nIn at least 62 countries, or roughly 32 percent of the world, same-sex relations and relationships are criminalized. Many countries also criminalize or otherwise prohibit cross-dressing and gender-affirming treatments for transgender individuals.\n**(4)**\nThe World Bank has begun to measure the macro-economic costs of criminal laws targeting LGBTQI individuals through lost productivity, detrimental health outcomes and violence, as a step toward mitigating those costs.\n**(5)**\nViolence and discrimination based on sexual orientation and gender identity are documented in the Department of State\u2019s annual Country Human Rights Reports to Congress. These reports continue to show a clear pattern of human rights violations, including murder, rape, torture, death threats, extortion, and imprisonment, in every region of the world based on sexual orientation and gender identity. In many instances police, prison, military, and civilian government authorities have been directly complicit in abuses aimed at LGBTQI citizens.\n**(6)**\nAs documented by the Department of State, LGBTQI individuals in many countries are subjected to capricious imprisonment, loss of employment, housing, and access to health care, societal stigma, and discrimination. LGBTQI-specific restrictions on basic freedoms of assembly, press, and speech exist in every region of the world.\n**(7)**\nTargeted sanctions are an important tool to push for accountability for violations of the human rights of LGBTQI people.\n**(8)**\nAnti-LGBTQI laws and discrimination pose significant risks for LGBTQI youth who come out to their family or community and often face rejection, homelessness, and limited educational and economic opportunities. These factors contribute to increased risks of substance abuse, suicide, and HIV infection among LGBTQI youth.\n**(9)**\nAnti-LGBTQI laws also increase global health risks. Studies have shown that when LGBTQI people, especially LGBTQI youth, face discrimination, they are less likely to seek HIV testing, prevention, and treatment services.\n**(10)**\nLGBTQI populations are disproportionately impacted by the Mexico City Policy, also widely referred to as the global gag rule . LGBTQI people often receive much of their health care through reproductive health clinics, and organizations that cannot comply with the policy are forced to discontinue work on United States-supported global health projects that are frequently used by LGBTQI populations, including HIV prevention and treatment, stigma reduction, and research.\n**(11)**\nAt the beginning of his second term, President Donald Trump reinstated the global gag rule before abruptly terminating nearly all foreign aid contracts.\n**(12)**\nBecause they face tremendous discrimination in the formal labor sector, many sex workers are also LGBTQI individuals, and many sex-worker-led programs and clinics serve the LGBTQI community with safe, non-stigmatizing, medical and social care. The United States Agency for International Development (USAID) has also referred to sex workers as a most-at-risk population . The anti-prostitution loyalty oath that health care providers receiving United States assistance must take isolates sex-worker-led and serving groups from programs and reinforces stigma, undermining both the global AIDS response and human rights. The Supreme Court found this requirement unconstitutional as it applies to United States nongovernmental organizations and their foreign affiliates in 2013.\n**(13)**\nAccording to the Trans Murder Monitoring Project, which monitors homicides of transgender individuals, there were at least 350 cases of reported killings of trans and gender-diverse people between October 1, 2023, and September 30, 2024.\n**(14)**\nIn many countries, intersex individuals experience prejudice and discrimination because their bodies do not conform to general expectations about sex and gender. Because of these expectations, medically unnecessary interventions are often performed in infancy without the consent or approval of intersex individuals, in violation of international human rights standards, and are then often denied official identification papers, blocking them from accessing basic services and legal protections.\n**(15)**\nAsylum and refugee protection are critical last-resort protections for LGBTQI individuals, but those who seek such protections face ostracization and abuse in refugee camps and detention facilities. They are frequently targeted for violence, including sexual assault, in refugee camps and in immigration detention. LGBTQI individuals may be segregated against their will for long periods in solitary confinement, in an effort to protect them from such violence, but prolonged solitary confinement itself represents an additional form of abuse that is profoundly damaging to the social and psychological well-being of any individual.\n**(16)**\nThe global COVID\u201319 pandemic exacerbated inequalities that LGBTQI individuals face, including access to health care, stigma, and discrimination, undermining LGBTQI rights around the world.\n**(17)**\nIn December 2011, President Barack Obama directed all Federal foreign affairs agencies to ensure that their diplomatic, humanitarian, health and foreign assistance programs take into account the needs of marginalized LGBTQI communities and persons.\n**(18)**\nIn 2015, the Department of State established the position of Special Envoy for the Human Rights of LGBTQI Persons.\n**(19)**\nIn 2021, President Joseph Biden issued the Memorandum on Advancing the Human Rights of Lesbian, Gay, Bisexual, Transgender, Queer, and Intersex Persons Around the World, which stated that it is the policy of the United States to pursue an end to violence and discrimination on the basis of sexual orientation, gender identity or expression, or sex characteristics and called for United States global leadership on LGBTQI rights.\n**(20)**\nIn Bostock v. Clayton County, the Supreme Court held that title VII of the Civil Rights Act of 1964 prohibits discrimination on the basis of gender identity and sexual orientation. On January 20, 2021, President Biden issued Executive Order 13988 to enforce Bostock, which orders all agency heads to determine the additional steps they should take to ensure that administration policies are fully implemented consistent with Bostock, including the Secretary of State and the Administrator of USAID.\n**(21)**\nThe use of United States diplomatic tools, including the Department of State\u2019s exchange and speaker programs, to address the human rights needs of marginalized communities has helped inform public debates in many countries regarding the protective responsibilities of any democratic government.\n**(22)**\nInclusion of human rights protections for LGBTQI individuals in United States trade agreements, as in the United States-Mexico-Canada Agreement, and trade preference programs is intended both to ensure a level playing field for United States business and to provide greater workplace protections overseas, compatible with those of the United States.\n**(23)**\nEngaging multilateral fora and international institutions is critical to impacting global norms and to broadening global commitments to fairer standards for the treatment of all people, including LGBTQI people. The United States must remain a leader in the United Nations system and has a vested interest in the success of that multilateral engagement.\n**(24)**\nUnited States participation in the Equal Rights Coalition, which is a new intergovernmental coalition of more than 40 governments and leading civil society organizations that work together to protect the human rights of LGBTQI people around the world, is vital to international efforts to respond to violence and impunity.\n**(25)**\nThose who represent the United States abroad, including our diplomats, development specialists and military, should reflect the diversity of our country and honor the United States call to equality, including through proud and open service abroad by LGBTQI United States citizens and those living with HIV.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Appropriations of the Senate;\n**(B)**\nthe Committee on Foreign Relations of the Senate;\n**(C)**\nthe Committee on the Judiciary of the Senate;\n**(D)**\nthe Committee on Appropriations of the House of Representatives;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(F)**\nthe Committee on the Judiciary of the House of Representatives.\n**(2) Gender identity**\nThe term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth.\n**(3) Lgbtqi**\nThe term LGBTQI means lesbian, gay, bisexual, transgender, queer, or intersex.\n**(4) Member of a vulnerable group**\nThe term member of a vulnerable group means an alien who\u2014\n**(A)**\nis younger than 21 years of age or older than 60 years of age;\n**(B)**\nis pregnant;\n**(C)**\nidentifies as lesbian, gay, bisexual, transgender, or intersex;\n**(D)**\nis victim or witness of a crime;\n**(E)**\nhas filed a nonfrivolous civil rights claim in Federal or State court;\n**(F)**\nhas a serious mental or physical illness or disability;\n**(G)**\nhas been determined by an asylum officer in an interview conducted under section 235(b)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1)(B) ) to have a credible fear of persecution; or\n**(H)**\nhas been determined by an immigration judge or the Secretary of Homeland Security to be experiencing severe trauma or to be a survivor of torture or gender-based violence, based on information obtained during intake, from the alien\u2019s attorney or legal service provider, or through credible self-reporting.\n**(5) Sexual orientation**\nThe term sexual orientation means actual or perceived homosexuality, heterosexuality, or bisexuality.\n#### 4. Documenting and responding to bias-motivated violence against LGBTQI people abroad\n##### (a) Information required To be included in annual country reports on human rights practices\n**(1) Section 116**\nSection 116(d) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151n(d) ) is amended\u2014\n**(A)**\nin paragraph (11)(C), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (12)(C)(ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(13) wherever applicable, the nature and extent of criminalization, discrimination, and violence by state and non-state actors based on sexual orientation or gender identity, as those terms are defined in section 3 of the GLOBE Act of 2025, or sex characteristics, including an identification of those countries that have adopted laws or constitutional provisions that criminalize or discriminate based on sexual orientation, gender identity, or sex characteristics, including descriptions of such laws and provisions. .\n**(2) Section 502b**\nSection 502B of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2304 ) is amended\u2014\n**(A)**\nby redesignating the second subsection (i) (relating to child marriage status) as subsection (j); and\n**(B)**\nby adding at the end the following:\n(k) Sexual orientation, gender identity, and sex characteristics The report required under subsection (b) shall include, wherever applicable, the nature and extent of criminalization, discrimination, and violence by state and non-state actors based on sexual orientation or gender identity, as those terms are defined in section 3 of the GLOBE Act of 2025, or sex characteristics, including an identification of those countries that have adopted laws or constitutional provisions that criminalize or discriminate based on sexual orientation, gender identity, or sex characteristics, including descriptions of such laws and provisions. .\n##### (b) Review at diplomatic and consular posts\n**(1) In general**\nIn preparing the annual country reports on human rights practices required under sections 116 and 502B of the Foreign Assistance Act of 1961, as amended by subsection (a), the Secretary of State shall obtain information from each diplomatic and consular post with respect to\u2014\n**(A)**\nincidents of violence against LGBTQI people in the country in which such post is located;\n**(B)**\nan analysis of the factors enabling or aggravating such incidents, such as government policy, societal pressure, or external actors; and\n**(C)**\nthe response, whether public or private, of the personnel of such post with respect to such incidents.\n**(2) Addressing bias-motivated violence**\nThe Secretary of State shall include in the annual strategic plans of the regional bureaus concrete diplomatic strategies, programs, and policies to address bias-motivated violence using information obtained pursuant to paragraph (1), such as programs to build capacity among civil society or governmental entities to document, investigate, and prosecute instances of such violence and provide support to victims of such violence.\n##### (c) Interagency group\n**(1) Establishment**\nThere is established an interagency group on responses to urgent threats to LGBTQI people in foreign countries (referred to in this subsection as the Interagency Group ), which shall be chaired by the Secretary of State and shall include the Secretary of Defense, the Secretary of the Treasury, the Administrator of the United States Agency for International Development, the Attorney General, and the head of each other Federal department or agency the President determines is relevant to the duties of the Interagency Group.\n**(2) Duties**\nThe duties of the Interagency Group shall be\u2014\n**(A)**\ncoordinating the responses of each participating agency with respect to threats directed towards LGBTQI populations in other countries;\n**(B)**\ndeveloping longer-term approaches to policy developments and incidents negatively impacting the LGBTQI populations in specific countries;\n**(C)**\nadvising the President on the designation of foreign persons for sanctions pursuant to section 5;\n**(D)**\nidentifying United States laws and policies, at the Federal, State, and local levels, that affirm the equality of LGBTQI persons; and\n**(E)**\nusing such laws and policies to develop diplomatic strategies to share the expertise obtained from the implementation of such laws and policies with appropriate officials of countries in which LGBTQI persons do not enjoy equal protection under the law.\n##### (d) Special envoy for the human rights of LGBTQI peoples\n**(1) Establishment**\nThe Secretary of State shall establish in the Bureau of Democracy, Human Rights, and Labor, the permanent position of Special Envoy for the Human Rights of LGBTQI Peoples (referred to in this section as the Special Envoy ), who\u2014\n**(A)**\nshall be appointed by the President; and\n**(B)**\nshall report directly to the Assistant Secretary for Democracy, Human Rights, and Lab.\n**(2) Rank**\nThe President may appoint the Special Envoy at the rank of Ambassador, by and with the advice and consent of the Senate.\n**(3) Purpose**\nThe Special Envoy shall direct efforts of the United States Government relating to United States foreign policy, as directed by the Secretary, regarding human rights abuses against LGBTQI people and communities internationally and the advancement of human rights for LGBTQI people, and shall represent the United States internationally in bilateral and multilateral engagement on such matters.\n**(4) Duties**\nThe Special Envoy shall\u2014\n**(A)**\nserve as the principal advisor to the Secretary of State regarding human rights for LGBTQI people internationally;\n**(B)**\nnotwithstanding any other provision of law, direct activities, policies, programs, and funding relating to the human rights of LGBTQI people and the advancement of LGBTQI equality initiatives internationally, for all bureaus and offices of the Department of State and shall lead the coordination of relevant international programs for all other Federal agencies relating to such matters;\n**(C)**\nrepresent the United States in diplomatic matters relevant to the human rights of LGBTQI people, including criminalization, discrimination, and violence against LGBTQI people internationally;\n**(D)**\ndirect, as appropriate, United States Government resources to respond to needs for protection, integration, resettlement, and empowerment of LGBTQI people in United States Government policies and international programs, including to prevent and respond to criminalization, discrimination, and violence against LGBTQI people internationally;\n**(E)**\ndesign, support, and implement activities regarding support, education, resettlement, and empowerment of LGBTQI people internationally, including for the prevention and response to criminalization, discrimination, and violence against LGBTQI people internationally;\n**(F)**\nlead interagency coordination between the foreign policy priorities related to the human rights of LGBTQI people and the development assistance priorities of the LGBTQI Coordinator of the United States Agency for International Development;\n**(G)**\nconduct regular consultation with nongovernmental organizations working to prevent and respond to criminalization, discrimination, and violence against LGBTQI people internationally; and\n**(H)**\nrepresent the United States in bilateral and multilateral fora on matters relevant to the human rights of LGBTQI people internationally, including criminalization, discrimination, and violence against LGBTQI people internationally.\n##### (e) Training at international law enforcement academies\nThe President shall ensure that any international law enforcement academy supported by United States assistance shall provide training with respect to the rights of LGBTQI people, including through specialized courses highlighting best practices in the documentation, investigation, and prosecution of bias-motivated hate crimes targeting persons based on actual or perceived sexual orientation, gender identity, or sex characteristics.\n##### (f) Senior LGBTQI coordinator\nThe Administrator of the United States Agency for International Development shall establish the permanent position of Senior LGBTQI Coordinator who shall be appointed by the Administrator and shall coordinate across the United States Agency for International Development with respect to LGBTQI inclusive development programming.\n#### 5. Sanctions on individuals responsible for violations of human rights against LGBTQI people\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act and biannually thereafter, the President shall submit to the appropriate congressional committees a list of each foreign person the President determines, based on credible information, including information obtained by other countries or by nongovernmental organizations that monitor violations of human rights\u2014\n**(1)**\nis responsible for or complicit in, with respect to persons based on actual or perceived sexual orientation, gender identity, or sex characteristics\u2014\n**(A)**\ntorture or cruel, inhuman, or degrading treatment or punishment;\n**(B)**\nprolonged detention without charges and trial;\n**(C)**\ncausing the disappearance of such persons by the abduction and clandestine detention of such persons; or\n**(D)**\nother flagrant denial of the right to life, liberty, or the security of such persons; or\n**(2)**\nacted as an agent of or on behalf of a foreign person in a matter relating to an activity described in paragraph (1).\n##### (b) Form; updates; removal\n**(1) Form**\nThe list required under subsection (a) shall be submitted in unclassified form and published in the Federal Register without regard to the requirements under section 222(f) of the Immigration and Nationality Act ( 8 U.S.C. 1202(f) ) with respect to confidentiality of records pertaining to the issuance or refusal of visas or permits to enter the United States, except that the President may include a foreign person in a classified, unpublished annex to such list if the President\u2014\n**(A)**\ndetermines\u2014\n**(i)**\nit is vital for the national security interests of the United States to include such foreign person; and\n**(ii)**\nthe use of such annex, and the inclusion of such person in such annex, would not undermine the overall purpose of this section to publicly identify foreign persons engaging in the conduct described in subsection (a) in order to increase accountability for such conduct; and\n**(B)**\nnot later than 15 days before including such person in a classified annex, provides to the relevant congressional committees notice of, and a justification for, including or continuing to include each foreign person in such annex despite the existence of any publicly available credible information indicating that each such foreign person engaged in an activity described in subsection (a).\n**(2) Updates**\nThe President shall submit to the relevant congressional committees an update of the list required under subsection (a) as new information becomes available.\n**(3) Removal**\nA foreign person may be removed from the list required under subsection (a) if the President determines and reports to the relevant congressional committees not later than 15 days before the removal of such person from such list that\u2014\n**(A)**\ncredible information exists that such person did not engage in the activity for which the person was included in such list;\n**(B)**\nsuch person has been prosecuted appropriately for the activity in which such person engaged;\n**(C)**\nsuch person has credibly demonstrated a significant change in behavior, has paid an appropriate consequence for the activities in which such person engaged, and has credibly committed to not engage in an activity described in subsection (a); or\n**(D)**\nremoval of such sanctions is in the vital national security interests of the United States.\n##### (c) Public submission of information\nThe President shall issue public guidance, including through United States diplomatic and consular posts, setting forth the manner by which the names of foreign persons that may meet the criteria to be included on the list required under subsection (a) may be submitted to the Department of State for evaluation.\n##### (d) Requests from chair and ranking member of relevant congressional committees\n**(1) Consideration of information**\nIn addition to the guidance issued pursuant to subsection (c), the President shall also consider information provided by the Chair or Ranking Member of each of the relevant congressional committees in determining whether to include a foreign person in the list required under subsection (a).\n**(2) Requests**\nNot later than 120 days after receiving a written request from the Chair or Ranking Member of 1 of the relevant congressional committees with respect to whether a foreign person meets the criteria for being included in the list required under subsection (a), the President shall transmit a response to such Chair or Ranking Member, as the case may be, with respect to the President\u2019s determination relating to such foreign person.\n**(3) Removal**\nIf the President removes from the list required under subsection (a) a foreign person that had been included in such list pursuant to a request under paragraph (2), the President shall provide to the relevant Chair or Ranking Member of 1 of the relevant congressional committees any information that contributed to such decision.\n**(4) Form**\nThe President may transmit a response required under paragraph (2) or paragraph (3) in classified form if the President determines such form is necessary for the national security interests of the United States.\n##### (e) Inadmissibility of certain individuals\n**(1) Ineligibility for visas and admission to the united states**\nA foreign person on the list required under subsection (a), and each immediate family member of such person, is\u2014\n**(A)**\ninadmissible to the United States;\n**(B)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(C)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(2) Current visas revoked**\n**(A) In general**\nThe issuing consular officer, the Secretary of State, or a designee of the Secretary of State, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), shall revoke any visa or other entry documentation issued to a foreign person on the list required under subsection (a), and any visa or other entry documentation issued to any immediate family member of such person, regardless of when the visa or other entry documentation was issued.\n**(B) Effect of revocation**\nA revocation under subparagraph (A) shall\u2014\n**(i)**\nhave immediate effect; and\n**(ii)**\nautomatically cancel any other valid visa or entry documentation that is in the foreign person\u2019s possession.\n**(C) Regulations required**\nNot later than 180 days after the date of enactment of this Act, the Secretary of State shall prescribe such regulations as are necessary to carry out this subsection.\n**(3) Sense of congress with respect to additional sanctions**\nIt is the sense of Congress that the President should impose additional targeted sanctions with respect to foreign persons on the list required under subsection (a) to push for accountability for flagrant denials of the right to life, liberty, or the security of the person, through the use of designations and targeted sanctions provided for such conduct under other existing authorities.\n**(4) Exceptions**\n**(A) Exception with respect to national security**\nThis section shall not apply with respect to\u2014\n**(i)**\nactivities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(ii)**\nany authorized intelligence or law enforcement activities of the United States.\n**(B) Exception to comply with international obligations**\nSanctions under this subsection shall not apply with respect to a foreign person if admitting or paroling such person into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success, June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(C) Exception for certain immediate family members**\n**(i) In general**\nA covered individual shall not be subject to sanctions under this section if the President certifies to the relevant congressional committees, in accordance with clause (ii), that such individual has a reasonable fear of persecution based on\u2014\n**(I)**\nactual or perceived sexual orientation, gender identity, or sex characteristics;\n**(II)**\nrace, religion, or nationality; or\n**(III)**\npolitical opinion or membership in a particular social group.\n**(ii) Determination and certification**\nA certification under clause (i) shall be made not later than 30 days after the date of the determination required by such clause. Any proceedings relating to such determination shall not be publicly available.\n**(iii) Covered individual**\nFor purposes of this subparagraph, the term covered individual means an individual who is an immediate family member of foreign person on the list required under subsection (a).\n**(5) Waivers in the interest of national security**\n**(A) In general**\nThe President may waive the application of paragraph (1) or (2) with respect to a foreign person included in the list required under subsection (a) if the President determines and transmits to the relevant congressional committees notice and justification, that such a waiver\u2014\n**(i)**\nis necessary to permit the United States to comply with the Agreement between the United Nations and the United States regarding the Headquarters of the United Nations, signed June 26, 1947, and entered into force November 21, 1947, or other applicable international obligations of the United States; or\n**(ii)**\nis in the national security interests of the United States.\n**(B) Timing of certain waivers**\nA waiver pursuant to a determination under clause (ii) of subparagraph (A) shall be transmitted not later than 15 days before the granting of such waiver.\n##### (f) Report to congress\nNot later than 1 year after the date of enactment of this Act and annually thereafter, the President, acting through the Secretary of State, shall submit to the relevant congressional committees a report that describes\u2014\n**(1)**\nthe actions taken to carry out this section, including\u2014\n**(A)**\nthe number of foreign persons added to or removed from the list required under subsection (a) during the year preceding each such report, the dates on which such persons were so added or removed, and the reasons for so adding or removing such persons; and\n**(B)**\nan analysis that compares increases or decreases in the number of such persons added or removed year-over-year and the reasons for such changes;\n**(2)**\nany efforts by the President to coordinate with the governments of other countries, as appropriate, to impose sanctions that are similar to the sanctions imposed under this section;\n**(3)**\nthe impact of the sanctions imposed under this section with respect to altering the behavior of each of the foreign persons included, as of the date of submission of the report, in the list required under subsection (a); and\n**(4)**\nsteps the Department of State can take to improve coordination with foreign governments, civil society groups, and the private sector, to prevent the commission of the human rights violations described in section 4(a)(1) against persons based on actual or perceived sexual orientation, gender identity, or sex characteristics.\n##### (g) Definitions\nIn this section:\n**(1) Foreign person**\nThe term foreign person has the meaning given such term in section 595.304 of title 31, Code of Federal Regulations (as in effect on the day before the date of the enactment of this Act).\n**(2) Immediate family member**\nThe term immediate family member has the meaning given such term for purposes of section 7031(c) of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2021 (division K of Public Law 116\u2013260 ).\n**(3) Person**\nThe term person has the meaning given such term in section 591.308 of title 31, Code of Federal Regulations (as in effect on the day before the date of the enactment of this Act).\n**(4) Relevant congressional committees**\nThe term relevant congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services of the Senate;\n**(B)**\nthe Committee on Foreign Relations of the Senate;\n**(C)**\nthe Committee on Homeland Security of the Senate;\n**(D)**\nthe Committee on the Judiciary of the Senate;\n**(E)**\nthe Committee on Armed Services of the House of Representatives;\n**(F)**\nthe Committee on Foreign Affairs of the House of Representatives;\n**(G)**\nthe Committee on Homeland Security of the House of Representatives; and\n**(H)**\nthe Committee on the Judiciary of the House of Representatives.\n#### 6. Combating international criminalization of LGBTQI status, expression, or conduct\n##### (a) Annual strategic review\nThe Secretary of State, in consultation with the Administrator of the United States Agency for International Development, during the course of annual strategic planning, shall include\u2014\n**(1)**\nan examination of the progress made in countries around the world toward the decriminalization of the status, expression, and conduct of LGBTQI individuals;\n**(2)**\nthe obstacles that remain toward achieving such decriminalization; and\n**(3)**\nthe strategies available to the Department of State and the United States Agency for International Development to address such obstacles.\n##### (b) Elements\nThe examination described in subsection (a) shall include the following:\n**(1)**\nAn examination of the full range of criminal and civil laws of other countries that disproportionately impact communities of LGBTQI individuals or apply with respect to the conduct of LGBTQI individuals.\n**(2)**\nIn consultation with the Attorney General, a list of countries in each geographic region with respect to which\u2014\n**(A)**\nthe Attorney General, acting through the Office of Overseas Prosecutorial Development Assistance and Training of the Department of Justice, shall prioritize programs seeking\u2014\n**(i)**\nto decriminalize the status, expression, and conduct of LGBTQI individuals;\n**(ii)**\nto monitor the trials of those prosecuted because of such status, expression, or conduct; and\n**(iii)**\nto reform related laws having a discriminatory impact on LGBTQI individuals; and\n**(B)**\napplicable speaker or exchange programs sponsored by the United States Government shall bring together civil society and governmental leaders to promote the recognition of LGBTQI rights through educational exchanges in the United States and support better understanding of the role that governments and civil societies mutually play in assurance of equal treatment of LGBTQI populations abroad.\n#### 7. Foreign assistance to protect human rights of LGBTQI people\n##### (a) Sense of congress\nIt is the sense of Congress that the full implementation of Executive Order 13988 (86 Fed. Reg. 7023) and the Supreme Court holding in Bostock v. Clayton County (140 S. Ct. 1731 (2020)) requires that United States foreign assistance and development organizations adopt the policy that no contractor, grantee, or implementing partner administering United States assistance for any humanitarian, development, or global health programs may discriminate against any employee or applicant for employment because of gender identity or sexual orientation.\n##### (b) Global equality fund\n**(1) In general**\nThe Secretary of State shall establish a fund, to be known as the Global Equality Fund (referred to in the section as the Fund ), which shall be managed by the Assistant Secretary of State for the Bureau of Democracy, Human Rights and Labor, consisting of such sums as may be appropriated to provide grants, emergency assistance, and technical assistance to eligible civil society organizations and human rights defenders working to advance and protect human rights for all including LGBTQI persons, by seeking\u2014\n**(A)**\nto ensure the freedoms of assembly, association, and expression;\n**(B)**\nto protect persons or groups against the threat of violence, including medically unnecessary interventions performed on intersex infants;\n**(C)**\nto advocate against laws that criminalize LGBTQI status, expression, or conduct or discriminate against individuals on the basis of sexual orientation, gender identity, or sex characteristics;\n**(D)**\nto end explicit and implicit forms of discrimination in the workplace, housing, education, and other public institutions or services; and\n**(E)**\nto build community awareness and support for the human rights of LGBTQI persons.\n**(2) Contributions**\nThe Secretary may accept financial and technical contributions from corporations, bilateral donors, foundations, nongovernmental organizations, and other entities supporting the outcomes described in paragraph (1), through the Fund.\n**(3) Prioritization**\nIn providing assistance through the Fund, the Secretary shall ensure due consideration and appropriate prioritization of assistance to groups that have historically been excluded from programs undertaken for the outcomes described in paragraph (1).\n##### (c) LGBTQI global development partnership\nThe Administrator of the United States Agency for International Development, in consultation with the Secretary of State, shall establish a partnership, which shall be known as the LGBTQI Global Development Partnership (referred to in this section as the Partnership ), to leverage the financial and technical contributions of corporations, bilateral donors, foundations, nongovernmental organizations, and universities to support the human rights and development of LGBTQI persons around the world by supporting programs, projects, and activities that\u2014\n**(1)**\nstrengthen the capacity of LGBTQI leaders and civil society organizations;\n**(2)**\ntrain LGBTQI leaders to effectively participate in democratic processes and lead civil institutions;\n**(3)**\nconduct research to inform national, regional, or global policies and programs; and\n**(4)**\npromote inclusive development, including economic empowerment through enhanced LGBTQI entrepreneurship and business development.\n##### (d) Consultation\nIn coordinating programs, projects, and activities through the Fund or the Partnership, the Secretary of State shall consult, as appropriate, with the Administrator of the United States Agency for International Development and the heads of other relevant Federal departments and agencies.\n##### (e) Report\nThe Secretary of State shall submit to the appropriate congressional committees an annual report that describes the work of, successes obtained, and challenges faced by the Fund and the Partnership established in accordance with this section.\n##### (f) Limitation on assistance relating to equal access\n**(1) In general**\nNone of the amounts authorized to be appropriated or otherwise made available to provide United States assistance for any humanitarian, development, or global health programs may be made available to any contractor, grantee, or implementing partner, unless such recipient\u2014\n**(A)**\nensures that the program, project, or activity funded by such amounts are made available to all elements of the population, except to the extent that such program, project, or activity targets a population because of the higher assessed risk of negative outcomes among such populations;\n**(B)**\nundertakes to make every reasonable effort to ensure that each subcontractor or subgrantee of such recipient will also adhere to the requirement described in subparagraph (A); and\n**(C)**\nagrees to return all amounts awarded or otherwise provided by the United States, including such additional penalties as the Secretary of State may determine to be appropriate, if the recipient is not able to adhere to the requirement described in subparagraph (A).\n**(2) Quarterly report**\nThe Secretary of State shall submit to the appropriate congressional committees a quarterly report describing the methods by which the Department monitors compliance with the requirement under paragraph (1)(A).\n##### (g) Office of foreign assistance\nThe Secretary of State, acting through the Director of the Office of Foreign Assistance, shall\u2014\n**(1)**\nmonitor the amount of foreign assistance obligated and expended on programs, projects, and activities relating to LGBTQI people; and\n**(2)**\nprovide the results of the indicators tracking such expenditure, upon request, to the Organization for Economic Co-operation and Development.\n#### 8. Global health inclusivity\n##### (a) In general\nThe Coordinator of United States Government Activities to Combat HIV/AIDS Globally (referred to in this section as the Coordinator ) shall\u2014\n**(1)**\ndevelop mechanisms to ensure that the President\u2019s Emergency Plan for AIDS Relief (PEPFAR) is implemented in a way that equitably serves LGBTQI people in accordance with the goals described in section 7(f), including by requiring all partner entities receiving assistance through PEPFAR to receive training on the health needs of and human rights standards relating to LGBTQI people; and\n**(2)**\npromptly notify Congress of any obstacles encountered by a foreign government or contractor, grantee, or implementing partner in the effort to equitably implement PEPFAR as described in section 7(f), including any remedial steps taken by the Coordinator to overcome such obstacles.\n##### (b) Report on international prosecutions for sex work or consensual sexual activity\nNot later than 180 days after the date of the enactment of this Act, the Coordinator shall submit to the appropriate congressional committees a report describing the manner in which commodities such as condoms provided by programs, projects, or activities funded through PEPFAR or other sources of United States assistance have been used as evidence to arrest, detain, or prosecute individuals in other countries in order to enforce domestic laws criminalizing sex work or consensual sexual activity.\n##### (c) Report on index testing related to HIV/AIDS\nNot later than 180 days after the date of the enactment of this Act, the Coordinator shall submit a report to the appropriate congressional committees describing the impact of partner notification services and index testing on treatment adherence, intimate partner violence, and exposure to the criminal justice system for key populations, including LGBTQI people and sex workers, using qualitative and quantitative data.\n##### (d) Report on impact of global gag rule\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit a report to the appropriate congressional committees describing the impact, as of the date of the submission of the report, on the implementation and enforcement of any iteration of the Mexico City Policy on the global LGBTQI community.\n##### (e) Removing limitations on eligibility for foreign assistance\n**(1) In general**\nNotwithstanding any other provision of law, regulation, or policy, in determining eligibility for assistance authorized under part I of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ), foreign nongovernmental organizations\u2014\n**(A)**\nshall not be ineligible for such assistance solely on the basis of health or medical services, including counseling and referral services, provided by such organizations with non-United States Government funds if such services do not violate the laws of the country in which they are being provided; and\n**(B)**\nshall not be subject to requirements relating to the use of non-United States Government funds for advocacy and lobbying activities other than those that apply to United States nongovernmental organizations receiving assistance under part I of such Act.\n**(2) Conforming amendments to pepfar authorization**\nSection 301 of the United States Leadership Against HIV/AIDS, Tuberculosis, and Malaria Act of 2003 ( 22 U.S.C. 7631 ) is amended\u2014\n**(A)**\nby striking subsections (d) through (f); and\n**(B)**\nby redesignating subsection (g) as subsection (d).\n**(3) Conforming amendments to the allocation of funds by the global aids coordinator**\nSection 403(a) of the United States Leadership Against HIV/AIDS, Tuberculosis, and Malaria Act of 2003 ( 22 U.S.C. 7673(a) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking shall\u2014 and all that follows through (A) provide and inserting shall provide ;\n**(ii)**\nby striking ; and and inserting a period; and\n**(iii)**\nby striking subparagraph (B); and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking Prevention strategy and all that follows through In carrying out paragraph (1) and inserting Prevention strategy ; and\n**(ii)**\nby striking subparagraph (B).\n**(4) Conforming amendments to tvpra authorization**\nSection 113 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7110 ) is amended\u2014\n**(A)**\nby striking subsection (g); and\n**(B)**\nby redesignating subsections (h) and (i) as subsections (g) and (h), respectively.\n#### 9. Immigration reform\n##### (a) Refugees and asylum seekers\n**(1) Lgbtqi social group**\nSection 101(a)(42) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(42) ) is amended by adding at the end the following: For purposes of determinations under this Act, a person who has been persecuted on the basis of sexual orientation or gender identity, shall be deemed to have been persecuted on account of membership in a particular social group, and a person who has a well-founded fear of persecution on the basis of sexual orientation or gender identity shall be deemed to have a well-founded fear of persecution on account of membership in a particular social group. .\n**(2) Report**\nSection 103(e) of the Immigration and Nationality Act ( 8 U.S.C. 1103(e) ) is amended\u2014\n**(A)**\nin paragraph (2), by striking \u201cdistrict office of the Service\u201d and inserting \u201cU.S. Citizenship and Immigration Services field office\u201d; and\n**(B)**\nby adding at the end the following:\n(3) Each annual report shall include information on the total number of applications for asylum and refugee status received that are, in whole or in part, based on persecution or a well-founded fear of persecution on account of sexual orientation or gender identity, and the rate of approval administratively of such applications. .\n**(3) Asylum filing deadline repeal**\n**(A) In general**\nSection 208(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a)(2) ) is amended\u2014\n**(i)**\nby striking subparagraph (B);\n**(ii)**\nby redesignating subparagraphs (C), (D), and (E) as subparagraphs (B), (C), and (D), respectively;\n**(iii)**\nin subparagraph (B), as redesignated, by striking (D) and inserting (C) .\n**(iv)**\nin subparagraph (C), as redesignated\u2014\n**(I)**\nby striking notwithstanding subparagraphs (B) and (C) and inserting notwithstanding subparagraph (B) ;\n**(II)**\nby striking either after Attorney General ; and\n**(III)**\nby striking or extraordinary circumstances relating to the delay in filing an application within the period specified in subparagraph (B) ; and\n**(v)**\nin subparagraph (D), as redesignated, by striking Subparagraphs (A) and (B) and inserting Subparagraph (A) .\n**(B) Application**\nThe amendments made by subparagraph (A) shall apply to applications for asylum filed before, on, or after the date of the enactment of this Act.\n##### (b) Permanent partners\nSection 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ) is amended\u2014\n**(1)**\nin paragraph (35)\u2014\n**(A)**\nby striking term and inserting terms ; and\n**(B)**\nby striking or husband do not and inserting and husband include any permanent partner, but do not ; and\n**(2)**\nby adding at the end the following:\n(53) The term marriage includes a permanent partnership. (54) The term permanent partner means an individual who is 18 years of age or older and\u2014 (A) is in a committed, intimate relationship with another individual who is 18 years of age or older, in which both parties intend a lifelong commitment; (B) is financially interdependent with the other individual; (C) is not married to anyone other than the other individual; (D) is a national of or, in the case of a person having no nationality, last habitually resided in a country that prohibits marriage between the individuals; and (E) is not a first-, second-, or third-degree blood relation of the other individual. (55) The term permanent partnership means the relationship that exists between 2 permanent partners. .\n##### (c) Counsel\n**(1) Appointment of counsel**\nSection 240(b)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(4) ) is amended\u2014\n**(A)**\nin subparagraph (B), by striking and at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting , and ; and\n**(C)**\nby adding at the end the following:\n(D) notwithstanding subparagraph (A), in a case in which an indigent alien requests representation, such representation shall be appointed by the court, at the expense of the Government, for such proceedings. .\n**(2) Right to counsel**\nSection 292 of the Immigration and Nationality Act ( 8 U.S.C. 1362 ) is amended\u2014\n**(A)**\nby inserting (a) before In any ;\n**(B)**\nby striking he and inserting the person ; and\n**(C)**\nby adding at the end the following:\n(b) Notwithstanding subsection (a), if an indigent alien requests representation, such representation shall be appointed by the court, at the expense of the Government, for the proceedings described in subsection (a). (c) In an interview relating to admission under section 207, an alien shall have the privilege of being represented, at no expense to the Government, by such counsel, authorized to practice in such proceedings, as the alien shall choose. .\n##### (d) Refugee admissions of LGBTQI aliens from certain countries\n**(1) In general**\nIn the case of aliens who are nationals of, or in the case of aliens having no nationality, last habitually resided in, a country that fails to protect against persecution on the basis of sexual orientation or gender identity and who share common characteristics that identify them as targets of persecution on account of sexual orientation or gender identity, such aliens are eligible for Priority 2 processing under the refugee resettlement priority system.\n**(2) Resettlement processing**\n**(A) In general**\nIf a refugee admitted under section 207 of the Immigration and Nationality Act discloses to an employee or contractor of the Bureau of Population, Refugees, and Migration information with respect to the refugee\u2019s sexual orientation or gender identity, the Secretary of State, with the refugee\u2019s consent, shall provide such information to the appropriate national resettlement agency\u2014\n**(i)**\nto prevent the refugee from being placed in a community in which the refugee is likely to face continued discrimination; and\n**(ii)**\nto place the refugee in a community that offers services to meet the needs of the refugee.\n**(B) Defined term**\nThe term national resettlement agency means an agency contracting with the Department of State to provide sponsorship and initial resettlement services to refugees entering the United States.\n##### (e) Training program\n**(1) Training program**\nIn order to create an environment in which an alien may safely disclose such alien\u2019s sexual orientation or gender identity, the Secretary of Homeland Security, in consultation with the Secretary of State, shall establish a training program for staff and translators who participate in the interview process of aliens seeking asylum or status as a refugee.\n**(2) Components of training program**\nThe training program described in paragraph (1) shall include instruction regarding\u2014\n**(A)**\nappropriate word choice and word usage;\n**(B)**\ncreating safe spaces and facilities for LGBTQI aliens;\n**(C)**\nconfidentiality requirements; and\n**(D)**\nnondiscrimination policies.\n##### (f) Limitation on detention\n**(1) Presumption of release**\n**(A) In general**\nNotwithstanding any other provision of law, except as provided in subparagraphs (B) and (C), the Secretary of Homeland Security\u2014\n**(i)**\nmay not detain an alien who is a member of a vulnerable group under any provision of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) pending a decision with respect to whether the alien is to be removed from the United States; and\n**(ii)**\nshall immediately release any detained alien who is a member of a vulnerable group.\n**(B) Exceptions**\nThe Secretary of Homeland Security may detain, pursuant to the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ), an alien who is a member of a vulnerable group if the Secretary determines, using credible and individualized information, that the use of alternatives to detention will not reasonably assure the appearance of the alien at removal proceedings, or that the alien is a threat to another person or the community. The fact that an alien has a criminal charge pending against the alien may not be the sole factor to justify the detention of the alien.\n**(C) Removal**\nIn a case in which detention is the least restrictive means of effectuating the removal from the United States of an alien who is a member of a vulnerable group, the subject of a final order of deportation or removal, and not detained under subparagraph (B), the Secretary of Homeland Security may, solely for the purpose of such removal, detain the alien for a period that is\u2014\n**(i)**\nthe shortest possible period immediately preceding the removal of the alien from the United States; and\n**(ii)**\nnot more than 5 days.\n**(2) Weekly review required**\n**(A) In general**\nNot less frequently than weekly, the Secretary of Homeland Security shall conduct an individualized review of each alien detained pursuant to paragraph (1)(B) to determine if the alien should continue to be detained under such paragraph.\n**(B) Release**\nIf the Secretary determines pursuant to subparagraph (A) that an alien should not be detained under paragraph (1)(B), the Secretary shall release the detainee not later than 24 hours after the date on which the Secretary makes such determination.\n##### (g) Protective custody for LGBTQI alien detainees\n**(1) Detainees**\nAn LGBTQI alien who is detained pursuant to subparagraph (B) or (C) of subsection (f)(1) may not be placed in housing that is segregated from the general population unless\u2014\n**(A)**\nthe alien requests placement in such housing for the protection of the alien; or\n**(B)**\nthe Secretary of Homeland Security determines, after assessing all available alternatives, that there is no available alternative means of separation from likely abusers.\n**(2) Placement factors**\nIf an LGBTQI alien is placed in segregated housing pursuant to paragraph (1), the Secretary of Homeland Security shall ensure that such housing\u2014\n**(A)**\nincludes non-LGBTQI aliens, to the extent practicable; and\n**(B)**\ncomplies with any applicable court order for the protection of LGBTQI aliens.\n**(3) Protective custody requests**\nIf an LGBTQI alien who is detained requests placement in segregated housing for the protection of such alien, the Secretary of Homeland Security shall grant such request.\n##### (h) Sense of congress\nIt is the sense of Congress that the Secretary of Homeland Security should hire a sufficient number of Refugee Corps officers to conduct refugee interviews within a reasonable period and to complete the adjudication of refugee petitions not later than 180 days after an alien files a request for Priority 2 consideration.\n#### 10. Issuance of passports and guarantee of citizenship to certain children born abroad\n##### (a) Sex identification markers\nFor the purposes of any identity document issued by the Department that displays sex information, including passports and consular reports of birth abroad, the Secretary shall ensure (through appropriate regulation, manual, policy, form, or other updates) that an applicant for such a document may self-select the sex designation, including a nonbinary or neutral designation, such as X .\n##### (b) Guarantee of citizenship to children born abroad using assistive reproduction technology\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall issue regulations, in accordance with the press statement released on May 18, 2021, with respect to U.S. Citizenship Transmission and Assisted Reproductive Technology , clarifying that no biological connection between a parent and a child is required for a child to acquire citizenship at birth from a United States citizen parent under subsections (c), (d), (e), and (g) of section 301 of the Immigration and Nationality Act ( 8 U.S.C. 1401 ), if the local law at the place of birth or United States law recognize such a person to be the legal parent of such child from birth.\n#### 11. Engaging international organizations in the fight against LGBTQI discrimination\n##### (a) Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States should be a leader in efforts by the United Nations to ensure that human rights norms, development principles, and political rights are fully inclusive of LGBTQI people;\n**(2)**\nUnited States leadership within international financial institutions, such as the World Bank and the regional development banks, should be used to ensure that the programs, projects, and activities undertaken by such institutions are fully inclusive of all people, including LGBTQI people; and\n**(3)**\nthe Secretary of State should seek appropriate opportunities to encourage the equal treatment of LGBTQI people during discussions with or participation in the full range of regional, multilateral, and international fora, such as the Organization of American States, the Organization for Security and Cooperation in Europe, the European Union, the African Union, and the Association of Southeast Asian Nations.\n##### (b) Action through the equal rights coalition\nThe Secretary of State shall promote diplomatic coordination through the Equal Rights Coalition, established in July 2016 at the Global LGBTQI Human Rights Conference in Montevideo, Uruguay, and other multilateral mechanisms, to achieve the goals and outcomes described in subsection (a).\n#### 12. Representing the rights of United States LGBTQI citizens deployed to diplomatic and consular posts\n##### (a) Sense of congress\nIt is the sense of Congress that, recognizing the importance of a diverse workforce in the representation of the United States abroad, and in support of sound personnel staffing policies, the Secretary of State should\u2014\n**(1)**\nprioritize efforts to ensure that foreign governments do not impede the assignment of United States LGBTQI citizens and their families to diplomatic and consular posts;\n**(2)**\nopen conversations with entities in the United States private sector that engage in business in other countries to the extent necessary to address any visa issues faced by such private sector entities with respect to their LGBTQI employees; and\n**(3)**\nprioritize efforts to improve post and post school information for LGBTQI employees and employees with LGBTQI family members.\n##### (b) Remedies for family visa denial\n**(1) In general**\nThe Secretary of State shall use all appropriate diplomatic efforts to ensure that the families of LGBTQI employees of the Department of State are issued visas from countries where such employees are posted.\n**(2) List required**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to Congress\u2014\n**(A)**\na classified list of each country that has refused to grant accreditation to LGBTQI employees of the Department of State or their family members in the prior 2 years; and\n**(B)**\nthe actions taken or intended to be taken by the Secretary, in accordance with paragraph (1), to ensure that LGBTQI employees are appointed to appropriate positions in accordance with diplomatic needs and personnel qualifications, including actions specifically relating to securing the accreditation of the families of such employees by relevant countries.\n##### (c) Improving post information and overseas environment for LGBTQI adults and children\n**(1) In general**\nThe Secretary of State shall ensure that LGBTQI employees of the Department of State and employees with LGBTQI family members have adequate information to pursue overseas postings, including country environment information for adults and children.\n**(2) Non-discrimination policies for united states government-supported schools**\nThe Secretary of State shall make every effort to ensure schools abroad that receive assistance and support from the United States Government under programs administered by the Office of Overseas Schools of the Department of State have active and clear nondiscrimination policies, including policies relating to sexual orientation and gender identity impacting LGBTQI children of all ages.\n**(3) Required information for lgbtqi children**\nThe Secretary of State shall ensure that information focused on LGBTQI children of all ages (including transgender and gender nonconforming students) is included in post reports, bidding materials, and Office of Overseas Schools reports, databases, and adequacy lists.",
      "versionDate": "2025-07-09",
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
        "actionDate": "2025-06-27",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4245",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GLOBE Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-07-29T21:54:13Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2231is.xml"
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
      "title": "GLOBE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-18T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GLOBE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-18T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Greater Leadership Overseas for the Benefit of Equality Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-18T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect human rights and enhance opportunities for LGBTQI people around the world, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-18T03:18:23Z"
    }
  ]
}
```
